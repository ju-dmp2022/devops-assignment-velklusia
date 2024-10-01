import ssl
from typing import Any, Dict, Optional, Union

import httpx
from attrs import define, evolve, field


@define
class Client:
    """A class for keeping track of data related to the API"""

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(alias="base_url")
    _cookies: Dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")
    _headers: Dict[str, str] = field(factory=dict, kw_only=True, alias="headers")
    _timeout: Optional[httpx.Timeout] = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: Union[str, bool, ssl.SSLContext] = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx_args: Dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx_args")
    _client: Optional[httpx.Client] = field(default=None, init=False)
    _async_client: Optional[httpx.AsyncClient] = field(default=None, init=False)

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx.Timeout) -> "Client":
        """Get a new client matching this one with a new timeout"""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)

    def set_httpx_client(self, client: httpx.Client) -> "Client":
        """Manually set the underlying httpx.Client"""
        self._client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "Client":
        """Enter a context manager for self.client"""
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx.Client"""
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "Client":
        """Manually set the underlying httpx.AsyncClient"""
        self._async_client = async_client
        return self

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client

    async def __aenter__(self) -> "Client":
        """Enter a context manager for underlying httpx.AsyncClient"""
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx.AsyncClient"""
        await self.get_async_httpx_client().__aexit__(*args, **kwargs)


@define
class AuthenticatedClient:
    """A Client which has been authenticated for use on secured endpoints"""

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(alias="base_url")
    _cookies: Dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")
    _headers: Dict[str, str] = field(factory=dict, kw_only=True, alias="headers")
    _timeout: Optional[httpx.Timeout] = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: Union[str, bool, ssl.SSLContext] = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx_args: Dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx_args")
    _client: Optional[httpx.Client] = field(default=None, init=False)
    _async_client: Optional[httpx.AsyncClient] = field(default=None, init=False)

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def with_headers(self, headers: Dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: Dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx.Timeout) -> "AuthenticatedClient":
        """Get a new client matching this one with a new timeout"""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)

    def set_httpx_client(self, client: httpx.Client) -> "AuthenticatedClient":
        """Manually set the underlying httpx.Client"""
        self._client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "AuthenticatedClient":
        """Enter a context manager for self.client"""
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx.Client"""
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "AuthenticatedClient":
        """Manually set the underlying httpx.AsyncClient"""
        self._async_client = async_client
        return self

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client

    async def __aenter__(self) -> "AuthenticatedClient":
        """Enter a context manager for underlying httpx.AsyncClient"""
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx.AsyncClient"""
        await self.get_async_httpx_client().__aexit__(*args, **kwargs)


@define
class CalculatorApi:
    """A class for interacting with the Calculator API"""

    client: Client

    def add(self, a: int, b: int) -> Any:
        """Perform addition"""
        response = self.client.get_httpx_client().post(
            "/add",
            json={"a": a, "b": b},
        )
        response.raise_for_status()
        return response.json()

    def subtract(self, a: int, b: int) -> Any:
        """Perform subtraction"""
        response = self.client.get_httpx_client().post(
            "/subtract",
            json={"a": a, "b": b},
        )
        response.raise_for_status()
        return response.json()

    def multiply(self, a: int, b: int) -> Any:
        """Perform multiplication"""
        response = self.client.get_httpx_client().post(
            "/multiply",
            json={"a": a, "b": b},
        )
        response.raise_for_status()
        return response.json()

    def divide(self, a: int, b: int) -> Any:
        """Perform division"""
        response = self.client.get_httpx_client().post(
            "/divide",
            json={"a": a, "b": b},
        )
        response.raise_for_status()
        return response.json()
