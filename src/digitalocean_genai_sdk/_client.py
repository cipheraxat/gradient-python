# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, DigitaloceanGenaiSDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import chat, genai, models, embeddings
    from .resources.chat import ChatResource, AsyncChatResource
    from .resources.models import ModelsResource, AsyncModelsResource
    from .resources.embeddings import EmbeddingsResource, AsyncEmbeddingsResource
    from .resources.genai.genai import GenaiResource, AsyncGenaiResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "DigitaloceanGenaiSDK",
    "AsyncDigitaloceanGenaiSDK",
    "Client",
    "AsyncClient",
]


class DigitaloceanGenaiSDK(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous DigitaloceanGenaiSDK client instance.

        This automatically infers the `api_key` argument from the `DIGITALOCEAN_GENAI_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("DIGITALOCEAN_GENAI_SDK_API_KEY")
        if api_key is None:
            raise DigitaloceanGenaiSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the DIGITALOCEAN_GENAI_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("DIGITALOCEAN_GENAI_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.digitalocean.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def genai(self) -> GenaiResource:
        from .resources.genai import GenaiResource

        return GenaiResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        from .resources.embeddings import EmbeddingsResource

        return EmbeddingsResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def with_raw_response(self) -> DigitaloceanGenaiSDKWithRawResponse:
        return DigitaloceanGenaiSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DigitaloceanGenaiSDKWithStreamedResponse:
        return DigitaloceanGenaiSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncDigitaloceanGenaiSDK(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncDigitaloceanGenaiSDK client instance.

        This automatically infers the `api_key` argument from the `DIGITALOCEAN_GENAI_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("DIGITALOCEAN_GENAI_SDK_API_KEY")
        if api_key is None:
            raise DigitaloceanGenaiSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the DIGITALOCEAN_GENAI_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("DIGITALOCEAN_GENAI_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.digitalocean.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def genai(self) -> AsyncGenaiResource:
        from .resources.genai import AsyncGenaiResource

        return AsyncGenaiResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        from .resources.embeddings import AsyncEmbeddingsResource

        return AsyncEmbeddingsResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncDigitaloceanGenaiSDKWithRawResponse:
        return AsyncDigitaloceanGenaiSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDigitaloceanGenaiSDKWithStreamedResponse:
        return AsyncDigitaloceanGenaiSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class DigitaloceanGenaiSDKWithRawResponse:
    _client: DigitaloceanGenaiSDK

    def __init__(self, client: DigitaloceanGenaiSDK) -> None:
        self._client = client

    @cached_property
    def genai(self) -> genai.GenaiResourceWithRawResponse:
        from .resources.genai import GenaiResourceWithRawResponse

        return GenaiResourceWithRawResponse(self._client.genai)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithRawResponse:
        from .resources.embeddings import EmbeddingsResourceWithRawResponse

        return EmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)


class AsyncDigitaloceanGenaiSDKWithRawResponse:
    _client: AsyncDigitaloceanGenaiSDK

    def __init__(self, client: AsyncDigitaloceanGenaiSDK) -> None:
        self._client = client

    @cached_property
    def genai(self) -> genai.AsyncGenaiResourceWithRawResponse:
        from .resources.genai import AsyncGenaiResourceWithRawResponse

        return AsyncGenaiResourceWithRawResponse(self._client.genai)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithRawResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithRawResponse

        return AsyncEmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)


class DigitaloceanGenaiSDKWithStreamedResponse:
    _client: DigitaloceanGenaiSDK

    def __init__(self, client: DigitaloceanGenaiSDK) -> None:
        self._client = client

    @cached_property
    def genai(self) -> genai.GenaiResourceWithStreamingResponse:
        from .resources.genai import GenaiResourceWithStreamingResponse

        return GenaiResourceWithStreamingResponse(self._client.genai)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import EmbeddingsResourceWithStreamingResponse

        return EmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)


class AsyncDigitaloceanGenaiSDKWithStreamedResponse:
    _client: AsyncDigitaloceanGenaiSDK

    def __init__(self, client: AsyncDigitaloceanGenaiSDK) -> None:
        self._client = client

    @cached_property
    def genai(self) -> genai.AsyncGenaiResourceWithStreamingResponse:
        from .resources.genai import AsyncGenaiResourceWithStreamingResponse

        return AsyncGenaiResourceWithStreamingResponse(self._client.genai)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithStreamingResponse

        return AsyncEmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)


Client = DigitaloceanGenaiSDK

AsyncClient = AsyncDigitaloceanGenaiSDK
