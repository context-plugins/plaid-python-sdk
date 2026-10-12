# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [ThePlaidApiClient](the_plaid_api/client.py)

<details>
<summary><code>def accounts_balance_get(body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints, such as `/accounts/get`, return a balance object,  `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid's other products. This endpoint can be used as long as Link has been initialized with any other product; `balance` itself is not a product that can be used to initialize Link. As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints (typically less than 10 seconds, but occasionally up to 30 seconds or more); if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

Note: If you are getting real-time balance for the purpose of assessing the return risk of a proposed ACH transaction, it is recommended to use `/signal/evaluate` instead of `/accounts/balance/get`. `/signal/evaluate` returns the same real-time balance information and also provides access to Signal Rules, which provides no-code transaction business logic configuration, backtesting and recommendations for tuning your transaction acceptance logic, and the ability to easily switch between Balance and Signal Transaction Scores as needed for ultra-low-latency, ML-powered risk assessments. For more details, see the [Balance documentation](https://plaid.com/docs/balance/#balance-integration-options).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.accounts_balance_get(
    AccountsBalanceGetRequest(
        access_token="string",
        secret="string",
        client_id="string",
        options=AccountsBalanceGetRequestOptions(account_ids=["string"]),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.accounts_balance_get(
    AccountsBalanceGetRequest(
        access_token="string",
        secret="string",
        client_id="string",
        options=AccountsBalanceGetRequestOptions(account_ids=["string"]),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountsBalanceGetRequest](the_plaid_api/models/accounts_balance_get_request.py) \| [AccountsBalanceGetRequestDict](the_plaid_api/models/accounts_balance_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def accounts_get(body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/accounts/get` endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts -- that is, accounts that are not closed and are capable of carrying a balance.
To return new accounts that were created after the user linked their Item, you can listen for the https://plaid.com/docs/api/items/#new_accounts_available webhook and then use Link's [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.

`/accounts/get` is free to use and retrieves cached information, rather than extracting fresh information from the institution. The balance returned will reflect the balance at the time of the last successful Item update. If the Item is enabled for a regularly updating product, such as Transactions, Investments, or Liabilities, the balance will typically update about once a day, as long as the Item is healthy. If the Item is enabled only for products that do not frequently update, such as Auth or Identity, balance data may be much older.

For real-time balance information, use the paid endpoints `/accounts/balance/get` or `/signal/evaluate` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.accounts_get(
    AccountsGetRequest(
        client_id="string",
        secret="string",
        access_token="string",
        options=AccountsGetRequestOptions(account_ids=["string"]),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.accounts_get(
    AccountsGetRequest(
        client_id="string",
        secret="string",
        access_token="string",
        options=AccountsGetRequestOptions(account_ids=["string"]),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountsGetRequest](the_plaid_api/models/accounts_get_request.py) \| [AccountsGetRequestDict](the_plaid_api/models/accounts_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def application_get(body: ApplicationGetRequest | ApplicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ApplicationGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.application_get(
    ApplicationGetRequest(
        client_id="some example string", secret="some example string", application_id="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApplicationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.application_get(
    ApplicationGetRequest(
        client_id="some example string", secret="some example string", application_id="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApplicationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ApplicationGetRequest](the_plaid_api/models/application_get_request.py) \| [ApplicationGetRequestDict](the_plaid_api/models/application_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ApplicationGetResponse](the_plaid_api/models/application_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ApplicationGetResponse](the_plaid_api/models/application_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_create(body: AssetReportAuditCopyCreateRequest | AssetReportAuditCopyCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportAuditCopyCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to the GSEs on your behalf if you participate in Fannie Mae's Day 1 Certainty™ program or utilize Freddie Mac's Loan Product Advisor® (LPA®) Asset and Income Modeler (AIM). An Audit Copy contains the same underlying data as the Asset Report.

To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You'll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_audit_copy_create(
    AssetReportAuditCopyCreateRequest(asset_report_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportAuditCopyCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_audit_copy_create(
    AssetReportAuditCopyCreateRequest(asset_report_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportAuditCopyCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportAuditCopyCreateRequest](the_plaid_api/models/asset_report_audit_copy_create_request.py) \| [AssetReportAuditCopyCreateRequestDict](the_plaid_api/models/asset_report_audit_copy_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportAuditCopyCreateResponse](the_plaid_api/models/asset_report_audit_copy_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportAuditCopyCreateResponse](the_plaid_api/models/asset_report_audit_copy_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_get(body: AssetReportAuditCopyGetRequest | AssetReportAuditCopyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/get`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_audit_copy_get(
    AssetReportAuditCopyGetRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_audit_copy_get(
    AssetReportAuditCopyGetRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportAuditCopyGetRequest](the_plaid_api/models/asset_report_audit_copy_get_request.py) \| [AssetReportAuditCopyGetRequestDict](the_plaid_api/models/asset_report_audit_copy_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_pdf_get(body: AssetReportAuditCopyPdfGetRequest | AssetReportAuditCopyPdfGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/audit_copy/pdf/get` endpoint retrieves an Asset Report Audit Copy in PDF format. The caller must provide the `audit_copy_token` that was shared via the `/asset_report/audit_copy/create` endpoint.

The response to `/asset_report/audit_copy/pdf/get` is the PDF binary data. The `request_id` is returned in the `Plaid-Request-ID` header.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_audit_copy_pdf_get(
    AssetReportAuditCopyPdfGetRequest(audit_copy_token="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_audit_copy_pdf_get(
    AssetReportAuditCopyPdfGetRequest(audit_copy_token="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportAuditCopyPdfGetRequest](the_plaid_api/models/asset_report_audit_copy_pdf_get_request.py) \| [AssetReportAuditCopyPdfGetRequestDict](the_plaid_api/models/asset_report_audit_copy_pdf_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_remove(body: AssetReportAuditCopyRemoveRequest | AssetReportAuditCopyRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportAuditCopyRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_audit_copy_remove(
    AssetReportAuditCopyRemoveRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportAuditCopyRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_audit_copy_remove(
    AssetReportAuditCopyRemoveRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportAuditCopyRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportAuditCopyRemoveRequest](the_plaid_api/models/asset_report_audit_copy_remove_request.py) \| [AssetReportAuditCopyRemoveRequestDict](the_plaid_api/models/asset_report_audit_copy_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportAuditCopyRemoveResponse](the_plaid_api/models/asset_report_audit_copy_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportAuditCopyRemoveResponse](the_plaid_api/models/asset_report_audit_copy_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_create(body: AssetReportCreateRequest | AssetReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.

The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. The exact amount of time to create the report will vary depending on how many days of history are requested and will typically range from a few seconds to about one minute. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).

The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_create(AssetReportCreateRequest(days_requested=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_create(AssetReportCreateRequest(days_requested=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportCreateRequest](the_plaid_api/models/asset_report_create_request.py) \| [AssetReportCreateRequestDict](the_plaid_api/models/asset_report_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportCreateResponse](the_plaid_api/models/asset_report_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportCreateResponse](the_plaid_api/models/asset_report_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_filter(body: AssetReportFilterRequest | AssetReportFilterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportFilterResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.

To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.

Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.

Plaid will fire a https://plaid.com/docs/api/products/assets/#product_ready webhook once generation of the filtered Asset Report has completed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_filter(
    AssetReportFilterRequest(asset_report_token="some example string", account_ids_to_exclude=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportFilterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_filter(
    AssetReportFilterRequest(asset_report_token="some example string", account_ids_to_exclude=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportFilterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportFilterRequest](the_plaid_api/models/asset_report_filter_request.py) \| [AssetReportFilterRequestDict](the_plaid_api/models/asset_report_filter_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportFilterResponse](the_plaid_api/models/asset_report_filter_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportFilterResponse](the_plaid_api/models/asset_report_filter_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_get(body: AssetReportGetRequest | AssetReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the https://plaid.com/docs/api/products/assets/#product_ready webhook to fire, indicating that the Report is ready to be retrieved.

By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report. To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.

For latency-sensitive applications, you can optionally call `/asset_report/create` with `options.add_ons` set to `["fast_assets"]`. This will cause Plaid to create two versions of the Asset Report: one with only current and available balance and identity information, and then later on the complete Asset Report. You will receive separate webhooks for each version of the Asset Report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_get(AssetReportGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_get(AssetReportGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportGetRequest](the_plaid_api/models/asset_report_get_request.py) \| [AssetReportGetRequestDict](the_plaid_api/models/asset_report_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_pdf_get(body: AssetReportPdfgetRequest | AssetReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the https://plaid.com/docs/api/products/assets/#product_ready webhook to fire, indicating that the Report is ready to be retrieved.

The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_pdf_get(
    AssetReportPdfgetRequest(asset_report_token="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_pdf_get(
    AssetReportPdfgetRequest(asset_report_token="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportPdfgetRequest](the_plaid_api/models/asset_report_pdfget_request.py) \| [AssetReportPdfgetRequestDict](the_plaid_api/models/asset_report_pdfget_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_refresh(body: AssetReportRefreshRequest | AssetReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.

The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_refresh(
    AssetReportRefreshRequest(asset_report_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_refresh(
    AssetReportRefreshRequest(asset_report_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportRefreshRequest](the_plaid_api/models/asset_report_refresh_request.py) \| [AssetReportRefreshRequestDict](the_plaid_api/models/asset_report_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportRefreshResponse](the_plaid_api/models/asset_report_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportRefreshResponse](the_plaid_api/models/asset_report_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_remove(body: AssetReportRemoveRequest | AssetReportRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.

The `/asset_report/remove` endpoint allows you to remove access to an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.asset_report_remove(
    AssetReportRemoveRequest(asset_report_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.asset_report_remove(
    AssetReportRemoveRequest(asset_report_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportRemoveRequest](the_plaid_api/models/asset_report_remove_request.py) \| [AssetReportRemoveRequestDict](the_plaid_api/models/asset_report_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportRemoveResponse](the_plaid_api/models/asset_report_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportRemoveResponse](the_plaid_api/models/asset_report_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def auth_get(body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AuthGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking, savings, and cash management accounts, along with high-level account data and balances when available.

Versioning note: In API version 2017-03-08, the schema of the `numbers` object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.auth_get(AuthGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.auth_get(AuthGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AuthGetRequest](the_plaid_api/models/auth_get_request.py) \| [AuthGetRequestDict](the_plaid_api/models/auth_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AuthGetResponse](the_plaid_api/models/auth_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AuthGetResponse](the_plaid_api/models/auth_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def auth_verify(body: AuthVerifyRequest | AuthVerifyRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AuthVerifyResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/auth/verify` endpoint verifies bank account and routing numbers and (optionally) account owner names against Plaid's database via [Database Auth](https://plaid.com/docs/auth/coverage/database-auth/). It can be used to verify account numbers that were not collected via the Plaid Link flow.

This endpoint is currently in Early Availability; contact sales or your Plaid account manager to request access.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.auth_verify(
    AuthVerifyRequest(
        numbers=AuthVerifyRequestNumbers(
            ach=AuthVerifyNumbersAch(account="some example string", routing="some example string")
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AuthVerifyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.auth_verify(
    AuthVerifyRequest(
        numbers=AuthVerifyRequestNumbers(
            ach=AuthVerifyNumbersAch(account="some example string", routing="some example string")
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AuthVerifyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AuthVerifyRequest](the_plaid_api/models/auth_verify_request.py) \| [AuthVerifyRequestDict](the_plaid_api/models/auth_verify_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AuthVerifyResponse](the_plaid_api/models/auth_verify_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AuthVerifyResponse](the_plaid_api/models/auth_verify_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_balance_get(body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferBalanceGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.

The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.

Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_balance_get(BankTransferBalanceGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferBalanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_balance_get(BankTransferBalanceGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferBalanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferBalanceGetRequest](the_plaid_api/models/bank_transfer_balance_get_request.py) \| [BankTransferBalanceGetRequestDict](the_plaid_api/models/bank_transfer_balance_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferBalanceGetResponse](the_plaid_api/models/bank_transfer_balance_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferBalanceGetResponse](the_plaid_api/models/bank_transfer_balance_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_cancel(body: BankTransferCancelRequest | BankTransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferCancelResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_cancel(
    BankTransferCancelRequest(bank_transfer_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_cancel(
    BankTransferCancelRequest(bank_transfer_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferCancelRequest](the_plaid_api/models/bank_transfer_cancel_request.py) \| [BankTransferCancelRequestDict](the_plaid_api/models/bank_transfer_cancel_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferCancelResponse](the_plaid_api/models/bank_transfer_cancel_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferCancelResponse](the_plaid_api/models/bank_transfer_cancel_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_create(body: BankTransferCreateRequest | BankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_create(
    BankTransferCreateRequest(
        idempotency_key="some example string",
        access_token="some example string",
        account_id="some example string",
        type_=BankTransferType.DEBIT,
        network=BankTransferNetwork.ACH,
        amount="some example string",
        iso_currency_code="some example string",
        description="some example string",
        user=BankTransferUser(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_create(
    BankTransferCreateRequest(
        idempotency_key="some example string",
        access_token="some example string",
        account_id="some example string",
        type_=BankTransferType.DEBIT,
        network=BankTransferNetwork.ACH,
        amount="some example string",
        iso_currency_code="some example string",
        description="some example string",
        user=BankTransferUser(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferCreateRequest](the_plaid_api/models/bank_transfer_create_request.py) \| [BankTransferCreateRequestDict](the_plaid_api/models/bank_transfer_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferCreateResponse](the_plaid_api/models/bank_transfer_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferCreateResponse](the_plaid_api/models/bank_transfer_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_event_list(body: BankTransferEventListRequest | BankTransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferEventListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/event/list` endpoint to get a list of Plaid-initiated ACH or bank transfer events based on specified filter criteria. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_event_list(BankTransferEventListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferEventListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_event_list(BankTransferEventListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferEventListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferEventListRequest](the_plaid_api/models/bank_transfer_event_list_request.py) \| [BankTransferEventListRequestDict](the_plaid_api/models/bank_transfer_event_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferEventListResponse](the_plaid_api/models/bank_transfer_event_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferEventListResponse](the_plaid_api/models/bank_transfer_event_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_event_sync(body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferEventSyncResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/bank_transfer/event/sync` allows you to request up to the next 25 Plaid-initiated bank transfer events that happened after a specific `event_id`. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_event_sync(BankTransferEventSyncRequest(after_id=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferEventSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_event_sync(BankTransferEventSyncRequest(after_id=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferEventSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferEventSyncRequest](the_plaid_api/models/bank_transfer_event_sync_request.py) \| [BankTransferEventSyncRequestDict](the_plaid_api/models/bank_transfer_event_sync_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferEventSyncResponse](the_plaid_api/models/bank_transfer_event_sync_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferEventSyncResponse](the_plaid_api/models/bank_transfer_event_sync_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_get(body: BankTransferGetRequest | BankTransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_get(BankTransferGetRequest(bank_transfer_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_get(
    BankTransferGetRequest(bank_transfer_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferGetRequest](the_plaid_api/models/bank_transfer_get_request.py) \| [BankTransferGetRequestDict](the_plaid_api/models/bank_transfer_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferGetResponse](the_plaid_api/models/bank_transfer_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferGetResponse](the_plaid_api/models/bank_transfer_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_list(body: BankTransferListRequest | BankTransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_list(BankTransferListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_list(BankTransferListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferListRequest](the_plaid_api/models/bank_transfer_list_request.py) \| [BankTransferListRequestDict](the_plaid_api/models/bank_transfer_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferListResponse](the_plaid_api/models/bank_transfer_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferListResponse](the_plaid_api/models/bank_transfer_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_migrate_account(body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferMigrateAccountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid account manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_migrate_account(
    BankTransferMigrateAccountRequest(
        account_number="some example string", routing_number="some example string", account_type="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferMigrateAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_migrate_account(
    BankTransferMigrateAccountRequest(
        account_number="some example string", routing_number="some example string", account_type="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferMigrateAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferMigrateAccountRequest](the_plaid_api/models/bank_transfer_migrate_account_request.py) \| [BankTransferMigrateAccountRequestDict](the_plaid_api/models/bank_transfer_migrate_account_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferMigrateAccountResponse](the_plaid_api/models/bank_transfer_migrate_account_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferMigrateAccountResponse](the_plaid_api/models/bank_transfer_migrate_account_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_sweep_get(body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferSweepGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_sweep_get(BankTransferSweepGetRequest(sweep_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferSweepGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_sweep_get(
    BankTransferSweepGetRequest(sweep_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferSweepGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferSweepGetRequest](the_plaid_api/models/bank_transfer_sweep_get_request.py) \| [BankTransferSweepGetRequestDict](the_plaid_api/models/bank_transfer_sweep_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferSweepGetResponse](the_plaid_api/models/bank_transfer_sweep_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferSweepGetResponse](the_plaid_api/models/bank_transfer_sweep_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_sweep_list(body: BankTransferSweepListRequest | BankTransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankTransferSweepListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.bank_transfer_sweep_list(BankTransferSweepListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferSweepListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.bank_transfer_sweep_list(BankTransferSweepListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankTransferSweepListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferSweepListRequest](the_plaid_api/models/bank_transfer_sweep_list_request.py) \| [BankTransferSweepListRequestDict](the_plaid_api/models/bank_transfer_sweep_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BankTransferSweepListResponse](the_plaid_api/models/bank_transfer_sweep_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankTransferSweepListResponse](the_plaid_api/models/bank_transfer_sweep_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_account_risk_evaluate(body: BeaconAccountRiskEvaluateRequest | BeaconAccountRiskEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconAccountRiskEvaluateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/beacon/account_risk/v1/evaluate` to get risk insights for a linked account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_account_risk_evaluate(BeaconAccountRiskEvaluateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconAccountRiskEvaluateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_account_risk_evaluate(BeaconAccountRiskEvaluateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconAccountRiskEvaluateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconAccountRiskEvaluateRequest](the_plaid_api/models/beacon_account_risk_evaluate_request.py) \| [BeaconAccountRiskEvaluateRequestDict](the_plaid_api/models/beacon_account_risk_evaluate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconAccountRiskEvaluateResponse](the_plaid_api/models/beacon_account_risk_evaluate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconAccountRiskEvaluateResponse](the_plaid_api/models/beacon_account_risk_evaluate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_duplicate_get(body: BeaconDuplicateGetRequest | BeaconDuplicateGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconDuplicateGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a Beacon Duplicate for a given Beacon Duplicate id.

A Beacon Duplicate represents a pair of similar Beacon Users within your organization.

Two Beacon User revisions are returned for each Duplicate record in either the `beacon_user1` or `beacon_user2` response fields.

The `analysis` field in the response indicates which fields matched between `beacon_user1` and `beacon_user2`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_duplicate_get(
    BeaconDuplicateGetRequest(beacon_duplicate_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconDuplicateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_duplicate_get(
    BeaconDuplicateGetRequest(beacon_duplicate_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconDuplicateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconDuplicateGetRequest](the_plaid_api/models/beacon_duplicate_get_request.py) \| [BeaconDuplicateGetRequestDict](the_plaid_api/models/beacon_duplicate_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconDuplicateGetResponse](the_plaid_api/models/beacon_duplicate_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconDuplicateGetResponse](the_plaid_api/models/beacon_duplicate_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_create(body: BeaconReportCreateRequest | BeaconReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconReportCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a fraud report for a given Beacon User.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_report_create(
    BeaconReportCreateRequest(
        beacon_user_id="some example string", type_=BeaconReportCreateType.FIRST_PARTY, fraud_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_report_create(
    BeaconReportCreateRequest(
        beacon_user_id="some example string", type_=BeaconReportCreateType.FIRST_PARTY, fraud_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconReportCreateRequest](the_plaid_api/models/beacon_report_create_request.py) \| [BeaconReportCreateRequestDict](the_plaid_api/models/beacon_report_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconReportCreateResponse](the_plaid_api/models/beacon_report_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconReportCreateResponse](the_plaid_api/models/beacon_report_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_get(body: BeaconReportGetRequest | BeaconReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a Beacon Report for a given Beacon Report ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_report_get(BeaconReportGetRequest(beacon_report_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_report_get(
    BeaconReportGetRequest(beacon_report_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconReportGetRequest](the_plaid_api/models/beacon_report_get_request.py) \| [BeaconReportGetRequestDict](the_plaid_api/models/beacon_report_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconReportGetResponse](the_plaid_api/models/beacon_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconReportGetResponse](the_plaid_api/models/beacon_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_list(body: BeaconReportListRequest | BeaconReportListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconReportListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/beacon/report/list` endpoint to view all Beacon Reports you created for a specific Beacon User. The reports returned by this endpoint are exclusively reports you created for a specific user. A Beacon User can only have one active report at a time, but a new report can be created if a previous report has been deleted. The results from this endpoint are paginated; the `next_cursor` field will be populated if there is another page of results that can be retrieved. To fetch the next page, pass the `next_cursor` value as the `cursor` parameter in the next request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_report_list(BeaconReportListRequest(beacon_user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_report_list(
    BeaconReportListRequest(beacon_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconReportListRequest](the_plaid_api/models/beacon_report_list_request.py) \| [BeaconReportListRequestDict](the_plaid_api/models/beacon_report_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconReportListResponse](the_plaid_api/models/beacon_report_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconReportListResponse](the_plaid_api/models/beacon_report_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_syndication_get(body: BeaconReportSyndicationGetRequest | BeaconReportSyndicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconReportSyndicationGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a Beacon Report Syndication for a given Beacon Report Syndication id.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_report_syndication_get(
    BeaconReportSyndicationGetRequest(beacon_report_syndication_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportSyndicationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_report_syndication_get(
    BeaconReportSyndicationGetRequest(beacon_report_syndication_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportSyndicationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconReportSyndicationGetRequest](the_plaid_api/models/beacon_report_syndication_get_request.py) \| [BeaconReportSyndicationGetRequestDict](the_plaid_api/models/beacon_report_syndication_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconReportSyndicationGetResponse](the_plaid_api/models/beacon_report_syndication_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconReportSyndicationGetResponse](the_plaid_api/models/beacon_report_syndication_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_syndication_list(body: BeaconReportSyndicationListRequest | BeaconReportSyndicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconReportSyndicationListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/beacon/report_syndication/list` endpoint to view all Beacon Reports that have been syndicated to a specific Beacon User. This endpoint returns Beacon Report Syndications which are references to Beacon Reports created either by you, or another Beacon customer, that matched the specified Beacon User. A Beacon User can have multiple active Beacon Report Syndications at once. The results from this endpoint are paginated; the `next_cursor` field will be populated if there is another page of results that can be retrieved. To fetch the next page, pass the `next_cursor` value as the `cursor` parameter in the next request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_report_syndication_list(
    BeaconReportSyndicationListRequest(beacon_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportSyndicationListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_report_syndication_list(
    BeaconReportSyndicationListRequest(beacon_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconReportSyndicationListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconReportSyndicationListRequest](the_plaid_api/models/beacon_report_syndication_list_request.py) \| [BeaconReportSyndicationListRequestDict](the_plaid_api/models/beacon_report_syndication_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconReportSyndicationListResponse](the_plaid_api/models/beacon_report_syndication_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconReportSyndicationListResponse](the_plaid_api/models/beacon_report_syndication_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_account_insights_get(body: BeaconUserAccountInsightsGetRequest | BeaconUserAccountInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconUserAccountInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Account Insights for all Accounts linked to this Beacon User. The insights for each account are computed based on the information that was last retrieved from the financial institution.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_user_account_insights_get(
    BeaconUserAccountInsightsGetRequest(beacon_user_id="some example string", access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserAccountInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_user_account_insights_get(
    BeaconUserAccountInsightsGetRequest(beacon_user_id="some example string", access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserAccountInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconUserAccountInsightsGetRequest](the_plaid_api/models/beacon_user_account_insights_get_request.py) \| [BeaconUserAccountInsightsGetRequestDict](the_plaid_api/models/beacon_user_account_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconUserAccountInsightsGetResponse](the_plaid_api/models/beacon_user_account_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconUserAccountInsightsGetResponse](the_plaid_api/models/beacon_user_account_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_create(body: BeaconUserCreateRequest | BeaconUserCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconUserCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create and scan a Beacon User against your Beacon Program, according to your program's settings.

When you submit a new user to `/beacon/user/create`, several checks are performed immediately:

  - The user's PII (provided within the `user` object) is searched against all other users within the Beacon Program you specified. If a match is found that violates your program's "Duplicate Information Filtering" settings, the user will be returned with a status of `pending_review`.

  - The user's PII is also searched against all fraud reports created by your organization across all of your Beacon Programs. If the user's data matches a fraud report that your team created, the user will be returned with a status of `rejected`.

  - Finally, the user's PII is searched against all fraud reports shared with the Beacon Network by other companies. If a matching fraud report is found, the user will be returned with a `pending_review` status if your program has enabled automatic flagging based on network fraud.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_user_create(
    BeaconUserCreateRequest(
        program_id="some example string",
        client_user_id="some example string",
        user=BeaconUserRequestData(
            name=BeaconUserName(given_name="some example string", family_name="some example string")
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_user_create(
    BeaconUserCreateRequest(
        program_id="some example string",
        client_user_id="some example string",
        user=BeaconUserRequestData(
            name=BeaconUserName(given_name="some example string", family_name="some example string")
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconUserCreateRequest](the_plaid_api/models/beacon_user_create_request.py) \| [BeaconUserCreateRequestDict](the_plaid_api/models/beacon_user_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconUserCreateResponse](the_plaid_api/models/beacon_user_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconUserCreateResponse](the_plaid_api/models/beacon_user_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_get(body: BeaconUserGetRequest | BeaconUserGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconUserGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch a Beacon User.

The Beacon User is returned with all of their associated information and a `status` based on the Beacon Network duplicate record and fraud checks.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_user_get(BeaconUserGetRequest(beacon_user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_user_get(
    BeaconUserGetRequest(beacon_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconUserGetRequest](the_plaid_api/models/beacon_user_get_request.py) \| [BeaconUserGetRequestDict](the_plaid_api/models/beacon_user_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconUserGetResponse](the_plaid_api/models/beacon_user_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconUserGetResponse](the_plaid_api/models/beacon_user_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_history_list(body: BeaconUserHistoryListRequest | BeaconUserHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconUserHistoryListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all changes to the Beacon User in reverse-chronological order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_user_history_list(
    BeaconUserHistoryListRequest(beacon_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserHistoryListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_user_history_list(
    BeaconUserHistoryListRequest(beacon_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserHistoryListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconUserHistoryListRequest](the_plaid_api/models/beacon_user_history_list_request.py) \| [BeaconUserHistoryListRequestDict](the_plaid_api/models/beacon_user_history_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconUserHistoryListResponse](the_plaid_api/models/beacon_user_history_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconUserHistoryListResponse](the_plaid_api/models/beacon_user_history_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_review(body: BeaconUserReviewRequest | BeaconUserReviewRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconUserGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the status of a Beacon User.

When updating a Beacon User's status via this endpoint, Plaid validates that the status change is consistent with the related state for this Beacon User. Specifically, we will check:

1. Whether there are any associated Beacon Reports connected to the Beacon User, and
2. Whether there are any confirmed Beacon Report Syndications connected to the Beacon User.

When updating a Beacon User's status to `rejected`, we enforce that either a Beacon Report has been created for the Beacon User or a Beacon Report Syndication has been confirmed.
When updating a Beacon User's status to `cleared`, we enforce that there are no active Beacon Reports or confirmed Beacon Report Syndications associated with the user. If you previously created a Beacon Report for this user, you must delete it before updating the Beacon User's status to `cleared`.
There are no restrictions on updating a Beacon User's status to `pending_review`.

If these conditions are not met, the request will be rejected with an error explaining the issue.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_user_review(
    BeaconUserReviewRequest(beacon_user_id="some example string", status=BeaconUserStatus.REJECTED)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_user_review(
    BeaconUserReviewRequest(beacon_user_id="some example string", status=BeaconUserStatus.REJECTED)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconUserReviewRequest](the_plaid_api/models/beacon_user_review_request.py) \| [BeaconUserReviewRequestDict](the_plaid_api/models/beacon_user_review_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconUserGetResponse](the_plaid_api/models/beacon_user_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconUserGetResponse](the_plaid_api/models/beacon_user_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_update(body: BeaconUserUpdateRequest | BeaconUserUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BeaconUserUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the identity data for a Beacon User in your Beacon Program or add new accounts to the Beacon User.

Similar to `/beacon/user/create`, several checks are performed immediately when you submit an identity data change to `/beacon/user/update`:

  - The user's updated PII is searched against all other users within the Beacon Program you specified. If a match is found that violates your program's "Duplicate Information Filtering" settings, the user will be returned with a status of `pending_review`.

  - The user's updated PII is also searched against all fraud reports created by your organization across all of your Beacon Programs. If the user's data matches a fraud report that your team created, the user will be returned with a status of `rejected`.

  - Finally, the user's PII is searched against all fraud reports shared with the Beacon Network by other companies. If a matching fraud report is found, the user will be returned with a `pending_review` status if your program has enabled automatic flagging based on network fraud.

Plaid maintains a version history for each Beacon User, so the Beacon User's identity data before and after the update is retained as separate versions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beacon_user_update(BeaconUserUpdateRequest(beacon_user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beacon_user_update(
    BeaconUserUpdateRequest(beacon_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BeaconUserUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BeaconUserUpdateRequest](the_plaid_api/models/beacon_user_update_request.py) \| [BeaconUserUpdateRequestDict](the_plaid_api/models/beacon_user_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BeaconUserUpdateResponse](the_plaid_api/models/beacon_user_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BeaconUserUpdateResponse](the_plaid_api/models/beacon_user_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_ewa_report_v1_get(body: BetaEwaReportV1GetRequest | BetaEwaReportV1GetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BetaEwaReportV1GetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/ewa_report/v1/get` endpoint provides an Earned Wage Access (EWA) score that quantifies the delinquency risk associated with a given item. The score is derived from a combination of cashflow patterns and network-based behavioral features.

The response returns a list of EWA scores, where each score corresponds to a potential advance amount range. These scores estimate the likelihood of repayment for advances within that range.

Score range: 1-99

Interpretation: Higher scores indicate a greater likelihood of repayment.

This endpoint enables clients to assess repayment risk and make data-driven decisions when determining eligibility or limits for earned wage advances.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beta_ewa_report_v1_get(
    BetaEwaReportV1GetRequest(access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaEwaReportV1GetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beta_ewa_report_v1_get(
    BetaEwaReportV1GetRequest(access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaEwaReportV1GetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BetaEwaReportV1GetRequest](the_plaid_api/models/beta_ewa_report_v1_get_request.py) \| [BetaEwaReportV1GetRequestDict](the_plaid_api/models/beta_ewa_report_v1_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BetaEwaReportV1GetResponse](the_plaid_api/models/beta_ewa_report_v1_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BetaEwaReportV1GetResponse](the_plaid_api/models/beta_ewa_report_v1_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_create(body: BetaPartnerCustomerV1CreateRequest | BetaPartnerCustomerV1CreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BetaPartnerCustomerV1CreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/partner/customer/v1/create` endpoint creates a new end customer record. You can provide as much information as you have available. If any required information is missing for the products you intend to use, it will be listed in the `requirements_due` field of the response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beta_partner_customer_v1_create(
    BetaPartnerCustomerV1CreateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        company_name="Plaid",
        products=[Products.AUTH, Products.IDENTITY],
        create_link_customization=True,
        legal_entity_name="Plaid",
        website="plaid.com",
        application_name="Plaid",
        technical_contact=PartnerEndCustomerTechnicalContact(
            given_name="Alice", family_name="Smith", email="alice.smith@example.com"
        ),
        billing_contact=PartnerEndCustomerBillingContact(
            given_name="Bob", family_name="Jones", email="bob.jones@example.com"
        ),
        customer_support_info=PartnerEndCustomerCustomerSupportInfo(
            email="support@example.com",
            phone_number="1234567890",
            contact_url="example.com/contact",
            link_update_url="example.com/update",
        ),
        address=PartnerEndCustomerAddress(
            city="New York", street="123 Main St", region="NY", postal_code="12345", country_code="US"
        ),
        redirect_uris=["http://localhost/oauth.html", "https://www.example.com/oauth.html"],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1CreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beta_partner_customer_v1_create(
    BetaPartnerCustomerV1CreateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        company_name="Plaid",
        products=[Products.AUTH, Products.IDENTITY],
        create_link_customization=True,
        legal_entity_name="Plaid",
        website="plaid.com",
        application_name="Plaid",
        technical_contact=PartnerEndCustomerTechnicalContact(
            given_name="Alice", family_name="Smith", email="alice.smith@example.com"
        ),
        billing_contact=PartnerEndCustomerBillingContact(
            given_name="Bob", family_name="Jones", email="bob.jones@example.com"
        ),
        customer_support_info=PartnerEndCustomerCustomerSupportInfo(
            email="support@example.com",
            phone_number="1234567890",
            contact_url="example.com/contact",
            link_update_url="example.com/update",
        ),
        address=PartnerEndCustomerAddress(
            city="New York", street="123 Main St", region="NY", postal_code="12345", country_code="US"
        ),
        redirect_uris=["http://localhost/oauth.html", "https://www.example.com/oauth.html"],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1CreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BetaPartnerCustomerV1CreateRequest](the_plaid_api/models/beta_partner_customer_v1_create_request.py) \| [BetaPartnerCustomerV1CreateRequestDict](the_plaid_api/models/beta_partner_customer_v1_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BetaPartnerCustomerV1CreateResponse](the_plaid_api/models/beta_partner_customer_v1_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BetaPartnerCustomerV1CreateResponse](the_plaid_api/models/beta_partner_customer_v1_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_enable(body: BetaPartnerCustomerV1EnableRequest | BetaPartnerCustomerV1EnableRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BetaPartnerCustomerV1EnableResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/partner/customer/v1/enable` endpoint is used by reseller partners to enable an end customer in the full Production environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beta_partner_customer_v1_enable(
    BetaPartnerCustomerV1EnableRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="634758733ebb4f00134b85ea",
        products=[Products.AUTH],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1EnableResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beta_partner_customer_v1_enable(
    BetaPartnerCustomerV1EnableRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="634758733ebb4f00134b85ea",
        products=[Products.AUTH],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1EnableResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BetaPartnerCustomerV1EnableRequest](the_plaid_api/models/beta_partner_customer_v1_enable_request.py) \| [BetaPartnerCustomerV1EnableRequestDict](the_plaid_api/models/beta_partner_customer_v1_enable_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BetaPartnerCustomerV1EnableResponse](the_plaid_api/models/beta_partner_customer_v1_enable_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BetaPartnerCustomerV1EnableResponse](the_plaid_api/models/beta_partner_customer_v1_enable_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_get(body: BetaPartnerCustomerV1GetRequest | BetaPartnerCustomerV1GetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BetaPartnerCustomerV1GetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/partner/customer/v1/get` endpoint is used by reseller partners to retrieve data about a single end customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beta_partner_customer_v1_get(
    BetaPartnerCustomerV1GetRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="634758733ebb4f00134b85ea",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1GetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beta_partner_customer_v1_get(
    BetaPartnerCustomerV1GetRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="634758733ebb4f00134b85ea",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1GetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BetaPartnerCustomerV1GetRequest](the_plaid_api/models/beta_partner_customer_v1_get_request.py) \| [BetaPartnerCustomerV1GetRequestDict](the_plaid_api/models/beta_partner_customer_v1_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BetaPartnerCustomerV1GetResponse](the_plaid_api/models/beta_partner_customer_v1_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BetaPartnerCustomerV1GetResponse](the_plaid_api/models/beta_partner_customer_v1_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_update(body: BetaPartnerCustomerV1UpdateRequest | BetaPartnerCustomerV1UpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BetaPartnerCustomerV1UpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/partner/customer/v1/update` endpoint updates an existing end customer record.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.beta_partner_customer_v1_update(
    BetaPartnerCustomerV1UpdateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="634758733ebb4f00134b85ea",
        bank_addendum_acceptance=PartnerEndCustomerBankAddendumAcceptance(
            customer_accepted=True,
            customer_ip_address="127.0.0.1",
            customer_agreement_timestamp=datetime(2025, 1, 1, 1, 0, 0, tzinfo=timezone.utc),
        ),
        questionnaires=PartnerEndCustomerQuestionnaires(
            cra=PartnerEndCustomerCraquestionnaire(
                purposes=PartnerEndCustomerCrapurposes(),
                is_third_party_involved=True,
                is_technical_service_provider_involved=True,
            ),
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1UpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.beta_partner_customer_v1_update(
    BetaPartnerCustomerV1UpdateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="634758733ebb4f00134b85ea",
        bank_addendum_acceptance=PartnerEndCustomerBankAddendumAcceptance(
            customer_accepted=True,
            customer_ip_address="127.0.0.1",
            customer_agreement_timestamp=datetime(2025, 1, 1, 1, 0, 0, tzinfo=timezone.utc),
        ),
        questionnaires=PartnerEndCustomerQuestionnaires(
            cra=PartnerEndCustomerCraquestionnaire(
                purposes=PartnerEndCustomerCrapurposes(),
                is_third_party_involved=True,
                is_technical_service_provider_involved=True,
            ),
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BetaPartnerCustomerV1UpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BetaPartnerCustomerV1UpdateRequest](the_plaid_api/models/beta_partner_customer_v1_update_request.py) \| [BetaPartnerCustomerV1UpdateRequestDict](the_plaid_api/models/beta_partner_customer_v1_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BetaPartnerCustomerV1UpdateResponse](the_plaid_api/models/beta_partner_customer_v1_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BetaPartnerCustomerV1UpdateResponse](the_plaid_api/models/beta_partner_customer_v1_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_verification_create(body: BusinessVerificationCreateRequest | BusinessVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BusinessVerificationCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new business verification to check a business's identity and risk profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.business_verification_create(
    BusinessVerificationCreateRequest(client_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BusinessVerificationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.business_verification_create(
    BusinessVerificationCreateRequest(client_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BusinessVerificationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BusinessVerificationCreateRequest](the_plaid_api/models/business_verification_create_request.py) \| [BusinessVerificationCreateRequestDict](the_plaid_api/models/business_verification_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BusinessVerificationCreateResponse](the_plaid_api/models/business_verification_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BusinessVerificationCreateResponse](the_plaid_api/models/business_verification_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_verification_get(body: BusinessVerificationGetRequest | BusinessVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BusinessVerificationGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the current state of a specific business verification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.business_verification_get(
    BusinessVerificationGetRequest(business_verification_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BusinessVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.business_verification_get(
    BusinessVerificationGetRequest(business_verification_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BusinessVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BusinessVerificationGetRequest](the_plaid_api/models/business_verification_get_request.py) \| [BusinessVerificationGetRequestDict](the_plaid_api/models/business_verification_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[BusinessVerificationGetResponse](the_plaid_api/models/business_verification_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BusinessVerificationGetResponse](the_plaid_api/models/business_verification_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_get(body: CashflowReportGetRequest | CashflowReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CashflowReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/cashflow_report/get` endpoint retrieves transactions data associated with an Item. Transactions data is standardized across financial institutions.
Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift. Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/cashflow_report/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).
Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `cursor` parameters in conjunction with the `has_more` response body field to fetch all available transactions.
Note that data isn't likely to be immediately available to `/cashflow_report/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `cashflow_report`, or if it wasn't, upon the first call to `/cashflow_report/refresh`. To be alerted when transaction data is ready to be fetched, listen for the `CASHFLOW_REPORT_READY` webhook.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cashflow_report_get(
    CashflowReportGetRequest(access_token="some example string", days_requested=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cashflow_report_get(
    CashflowReportGetRequest(access_token="some example string", days_requested=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CashflowReportGetRequest](the_plaid_api/models/cashflow_report_get_request.py) \| [CashflowReportGetRequestDict](the_plaid_api/models/cashflow_report_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CashflowReportGetResponse](the_plaid_api/models/cashflow_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CashflowReportGetResponse](the_plaid_api/models/cashflow_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_insights_get(body: CashflowReportInsightsGetRequest | CashflowReportInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CashflowReportInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/cashflow_report/insights/get` endpoint retrieves insights data associated with an Item. Insights are only calculated on credit and depository accounts.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cashflow_report_insights_get(
    CashflowReportInsightsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cashflow_report_insights_get(
    CashflowReportInsightsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CashflowReportInsightsGetRequest](the_plaid_api/models/cashflow_report_insights_get_request.py) \| [CashflowReportInsightsGetRequestDict](the_plaid_api/models/cashflow_report_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CashflowReportInsightsGetResponse](the_plaid_api/models/cashflow_report_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CashflowReportInsightsGetResponse](the_plaid_api/models/cashflow_report_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_refresh(body: CashflowReportRefreshRequest | CashflowReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CashflowReportRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cashflow_report/refresh` is an endpoint that initiates an on-demand extraction to fetch the newest transactions for an Item (given an `item_id`). The Item must already have Cashflow Report added as a product in order to call `/cashflow_report/refresh`.

After calling `/cashflow_report/refresh`, Plaid will fire a webhook `CASHFLOW_REPORT_READY` alerting clients that new transactions data can then be ingested via `/cashflow_report/get` or the webhook will contain an error code informing there was an error in refreshing transactions data.

Note that the `/cashflow_report/refresh` endpoint is not supported for Capital One (`ins_128026`) non-depository accounts and will result in a `PRODUCTS_NOT_SUPPORTED` error if called on an Item that contains only non-depository accounts from that institution.

As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints (typically less than 10 seconds, but up to 30 seconds or more). If you encounter errors, you may find it necessary to adjust your timeout period for requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cashflow_report_refresh(
    CashflowReportRefreshRequest(access_token="some example string", days_requested=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cashflow_report_refresh(
    CashflowReportRefreshRequest(access_token="some example string", days_requested=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CashflowReportRefreshRequest](the_plaid_api/models/cashflow_report_refresh_request.py) \| [CashflowReportRefreshRequestDict](the_plaid_api/models/cashflow_report_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CashflowReportRefreshResponse](the_plaid_api/models/cashflow_report_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CashflowReportRefreshResponse](the_plaid_api/models/cashflow_report_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_transactions_get(body: CashflowReportTransactionsGetRequest | CashflowReportTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CashflowReportTransactionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/cashflow_report/transactions/get` endpoint retrieves transactions data associated with an Item. Transactions data is standardized across financial institutions.
Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift. Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/cashflow_report/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).
Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `cursor` parameters in conjunction with the `has_more` response body field to fetch all available transactions.
Note that data isn't likely to be immediately available to `/cashflow_report/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `cashflow_report`, or if it wasn't, upon the first call to `/cashflow_report/refresh`. To be alerted when transaction data is ready to be fetched, listen for the `CASHFLOW_REPORT_READY` webhook.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cashflow_report_transactions_get(
    CashflowReportTransactionsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cashflow_report_transactions_get(
    CashflowReportTransactionsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CashflowReportTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CashflowReportTransactionsGetRequest](the_plaid_api/models/cashflow_report_transactions_get_request.py) \| [CashflowReportTransactionsGetRequestDict](the_plaid_api/models/cashflow_report_transactions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CashflowReportTransactionsGetResponse](the_plaid_api/models/cashflow_report_transactions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CashflowReportTransactionsGetResponse](the_plaid_api/models/cashflow_report_transactions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def categories_get(body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CategoriesGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a request to the `/categories/get` endpoint to get detailed information on legacy categories returned by Plaid. This endpoint does not require authentication.

All implementations are recommended to https://plaid.com/docs/transactions/pfc-migration/ instead of the legacy `category` taxonomy supported by this endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.categories_get({})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CategoriesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.categories_get({})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CategoriesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CategoriesGetResponse](the_plaid_api/models/categories_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CategoriesGetResponse](the_plaid_api/models/categories_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def consent_events_get(body: ConsentEventsGetRequest | ConsentEventsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConsentEventsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List a historical log of Item consent events. Consent logs are only available for events occurring on or after November 7, 2024. Extremely recent events (occurring within the past 12 hours) may not be available via this endpoint. Up to three years of consent logs will be available via the endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.consent_events_get(ConsentEventsGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConsentEventsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.consent_events_get(
    ConsentEventsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConsentEventsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ConsentEventsGetRequest](the_plaid_api/models/consent_events_get_request.py) \| [ConsentEventsGetRequestDict](the_plaid_api/models/consent_events_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ConsentEventsGetResponse](the_plaid_api/models/consent_events_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConsentEventsGetResponse](the_plaid_api/models/consent_events_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def consumer_report_pdf_get(body: ConsumerReportPdfgetRequest | ConsumerReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves all existing CRB Bank Income and Base reports for the consumer in PDF format.

Response is PDF binary data. The `request_id` is returned in the `Plaid-Request-ID` header.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.consumer_report_pdf_get(ConsumerReportPdfgetRequest(user_token="some example string"))
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.consumer_report_pdf_get(
    ConsumerReportPdfgetRequest(user_token="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ConsumerReportPdfgetRequest](the_plaid_api/models/consumer_report_pdfget_request.py) \| [ConsumerReportPdfgetRequestDict](the_plaid_api/models/consumer_report_pdfget_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_base_report_get(body: CraCheckReportBaseReportGetRequest | CraCheckReportBaseReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportBaseReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve the Base Report for your user, allowing you to receive comprehensive bank account and cash flow data. You should call this endpoint after you've received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook, either after the Link session for the user or after calling `/cra/check_report/create`. If the most recent consumer report for the user doesn't have sufficient data to generate the base report, or the consumer report has expired, you will receive an error indicating that you should create a new consumer report by calling `/cra/check_report/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_base_report_get(CraCheckReportBaseReportGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportBaseReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_base_report_get(CraCheckReportBaseReportGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportBaseReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportBaseReportGetRequest](the_plaid_api/models/cra_check_report_base_report_get_request.py) \| [CraCheckReportBaseReportGetRequestDict](the_plaid_api/models/cra_check_report_base_report_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportBaseReportGetResponse](the_plaid_api/models/cra_check_report_base_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportBaseReportGetResponse](the_plaid_api/models/cra_check_report_base_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_cashflow_insights_get(body: CraCheckReportCashflowInsightsGetRequest | CraCheckReportCashflowInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportCashflowInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve the Cashflow Insights report for your user. You should call this endpoint after you've received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook, either after the Link session for the user or after calling `/cra/check_report/create`. If the most recent consumer report for the user doesn't have sufficient data to generate the report, or the consumer report has expired, you will receive an error indicating that you should create a new consumer report by calling `/cra/check_report/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_cashflow_insights_get(CraCheckReportCashflowInsightsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportCashflowInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_cashflow_insights_get(
    CraCheckReportCashflowInsightsGetRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportCashflowInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportCashflowInsightsGetRequest](the_plaid_api/models/cra_check_report_cashflow_insights_get_request.py) \| [CraCheckReportCashflowInsightsGetRequestDict](the_plaid_api/models/cra_check_report_cashflow_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportCashflowInsightsGetResponse](the_plaid_api/models/cra_check_report_cashflow_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportCashflowInsightsGetResponse](the_plaid_api/models/cra_check_report_cashflow_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_create(body: CraCheckReportCreateRequest | CraCheckReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/cra/check_report/create` to refresh data in an existing report. A Consumer Report will last for 24 hours before expiring; you should call any `/get` endpoints on the report before it expires. If a report expires, you can call `/cra/check_report/create` again to re-generate it and refresh the data in the report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_create(
    CraCheckReportCreateRequest(
        webhook="some example string",
        days_requested=1,
        consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_create(
    CraCheckReportCreateRequest(
        webhook="some example string",
        days_requested=1,
        consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportCreateRequest](the_plaid_api/models/cra_check_report_create_request.py) \| [CraCheckReportCreateRequestDict](the_plaid_api/models/cra_check_report_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportCreateResponse](the_plaid_api/models/cra_check_report_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportCreateResponse](the_plaid_api/models/cra_check_report_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_income_insights_get(body: CraCheckReportIncomeInsightsGetRequest | CraCheckReportIncomeInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportIncomeInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve the Income Insights report for your user. You should call this endpoint after you've received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook, either after the Link session for the user or after calling `/cra/check_report/create`. If the most recent consumer report for the user doesn't have sufficient data to generate the report, or the consumer report has expired, you will receive an error indicating that you should create a new consumer report by calling `/cra/check_report/create`.

NOTE: The following schema was updated in April 2026 to reflect the response when the provided version is "II2". Please see [this document](https://docs.google.com/document/d/1kQkQ7FOgFaC4n-sUGUk74hoXZNY_L_nJeCuMe7Keip4/edit?tab=t.0#heading=h.rudamzinus2i) for guidance on migrating to II2 if you are currently using the II1 version, and [this section](https://docs.google.com/document/d/1kQkQ7FOgFaC4n-sUGUk74hoXZNY_L_nJeCuMe7Keip4/edit?tab=t.0#bookmark=id.tdcc2wpk0h60) for an example II1 response along with its [documentation](https://docs.google.com/document/d/1kQkQ7FOgFaC4n-sUGUk74hoXZNY_L_nJeCuMe7Keip4/edit?tab=t.36c85n2ircqk#heading=h.79dwr5c1iszl).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_income_insights_get(CraCheckReportIncomeInsightsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportIncomeInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_income_insights_get(
    CraCheckReportIncomeInsightsGetRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportIncomeInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportIncomeInsightsGetRequest](the_plaid_api/models/cra_check_report_income_insights_get_request.py) \| [CraCheckReportIncomeInsightsGetRequestDict](the_plaid_api/models/cra_check_report_income_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportIncomeInsightsGetResponse](the_plaid_api/models/cra_check_report_income_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportIncomeInsightsGetResponse](the_plaid_api/models/cra_check_report_income_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_lend_score_get(body: CraCheckReportLendScoreGetRequest | CraCheckReportLendScoreGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportLendScoreGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve the LendScore report for your user. You should call this endpoint after you've received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook, either after the Link session for the user or after calling `/cra/check_report/create`. If the most recent consumer report for the user doesn't have sufficient data to generate the report, or the consumer report has expired, you will receive an error indicating that you should create a new consumer report by calling `/cra/check_report/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_lend_score_get(CraCheckReportLendScoreGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportLendScoreGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_lend_score_get(CraCheckReportLendScoreGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportLendScoreGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportLendScoreGetRequest](the_plaid_api/models/cra_check_report_lend_score_get_request.py) \| [CraCheckReportLendScoreGetRequestDict](the_plaid_api/models/cra_check_report_lend_score_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportLendScoreGetResponse](the_plaid_api/models/cra_check_report_lend_score_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportLendScoreGetResponse](the_plaid_api/models/cra_check_report_lend_score_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_network_insights_get(body: CraCheckReportNetworkInsightsGetRequest | CraCheckReportNetworkInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportNetworkInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve the Network Insights report for your user. You should call this endpoint after you've received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook, either after the Link session for the user or after calling `/cra/check_report/create`. If the most recent consumer report for the user doesn't have sufficient data to generate the report, or the consumer report has expired, you will receive an error indicating that you should create a new consumer report by calling `/cra/check_report/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_network_insights_get(CraCheckReportNetworkInsightsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportNetworkInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_network_insights_get(
    CraCheckReportNetworkInsightsGetRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportNetworkInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportNetworkInsightsGetRequest](the_plaid_api/models/cra_check_report_network_insights_get_request.py) \| [CraCheckReportNetworkInsightsGetRequestDict](the_plaid_api/models/cra_check_report_network_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportNetworkInsightsGetResponse](the_plaid_api/models/cra_check_report_network_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportNetworkInsightsGetResponse](the_plaid_api/models/cra_check_report_network_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_partner_insights_get(body: CraCheckReportPartnerInsightsGetRequest | CraCheckReportPartnerInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportPartnerInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve the Partner Insights report for your user. You should call this endpoint after you've received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook, either after the Link session for the user or after calling `/cra/check_report/create`. If the most recent consumer report for the user doesn't have sufficient data to generate the report, or the consumer report has expired, you will receive an error indicating that you should create a new consumer report by calling `/cra/check_report/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_partner_insights_get(CraCheckReportPartnerInsightsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportPartnerInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_partner_insights_get(
    CraCheckReportPartnerInsightsGetRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportPartnerInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportPartnerInsightsGetRequest](the_plaid_api/models/cra_check_report_partner_insights_get_request.py) \| [CraCheckReportPartnerInsightsGetRequestDict](the_plaid_api/models/cra_check_report_partner_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportPartnerInsightsGetResponse](the_plaid_api/models/cra_check_report_partner_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportPartnerInsightsGetResponse](the_plaid_api/models/cra_check_report_partner_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_pdf_get(body: CraCheckReportPdfgetRequest | CraCheckReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/check_report/pdf/get` retrieves the most recent Consumer Report in PDF format. By default, the most recent Base Report (if it exists) for the user will be returned. To request that the most recent Partner Insights or Income Insights report be included in the PDF as well, use the `add-ons` field.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_pdf_get(CraCheckReportPdfgetRequest())
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_pdf_get(CraCheckReportPdfgetRequest())
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportPdfgetRequest](the_plaid_api/models/cra_check_report_pdfget_request.py) \| [CraCheckReportPdfgetRequestDict](the_plaid_api/models/cra_check_report_pdfget_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_verification_get(body: CraCheckReportVerificationGetRequest | CraCheckReportVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCheckReportVerificationGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve home lending reports for a user. To obtain a VoA or Employment Refresh report, you need to make sure that `cra_base_report` is included in the `products` parameter when calling `/link/token/create` or `/cra/check_report/create`.

You should call this endpoint after you've received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook, either after the Link session for the user or after calling `/cra/check_report/create`.

If the most recent consumer report for the user doesn't have sufficient data to generate the report, or the consumer report has expired, you will receive an error indicating that you should create a new consumer report by calling `/cra/check_report/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_verification_get(
    CraCheckReportVerificationGetRequest(reports_requested=[CraCheckReportVerificationGetReportType.VOA])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_verification_get(
    CraCheckReportVerificationGetRequest(reports_requested=[CraCheckReportVerificationGetReportType.VOA])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCheckReportVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportVerificationGetRequest](the_plaid_api/models/cra_check_report_verification_get_request.py) \| [CraCheckReportVerificationGetRequestDict](the_plaid_api/models/cra_check_report_verification_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCheckReportVerificationGetResponse](the_plaid_api/models/cra_check_report_verification_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCheckReportVerificationGetResponse](the_plaid_api/models/cra_check_report_verification_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_verification_pdf_get(body: CraCheckReportVerificationPdfGetRequest | CraCheckReportVerificationPdfGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/cra/check_report/verification/pdf/get` endpoint retrieves the most recent Consumer Report in PDF format, specifically formatted for Home Lending verification use cases. Before calling this endpoint, ensure that you've created a VOA report through Link or the `/cra/check_report/create` endpoint, and have received a `CHECK_REPORT_READY` or a `USER_CHECK_REPORT_READY` webhook.

The response to `/cra/check_report/verification/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_check_report_verification_pdf_get(CraCheckReportVerificationPdfGetRequest())
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_check_report_verification_pdf_get(
    CraCheckReportVerificationPdfGetRequest()
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCheckReportVerificationPdfGetRequest](the_plaid_api/models/cra_check_report_verification_pdf_get_request.py) \| [CraCheckReportVerificationPdfGetRequestDict](the_plaid_api/models/cra_check_report_verification_pdf_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_credit_profile_report_get(body: CraCreditProfileReportGetRequest | CraCreditProfileReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraCreditProfileReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/credit_profile/report/get` retrieves a credit profile report for a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_credit_profile_report_get(
    CraCreditProfileReportGetRequest(
        user_id="some example string",
        consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
        client_report_id="some example string",
        report_type=CraCreditProfileReportType.QUALIFY,
        inquiry_type=CraCreditProfileInquiryType.SOFT_INQUIRY,
        version=CraCreditProfileReportVersion.V1,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCreditProfileReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_credit_profile_report_get(
    CraCreditProfileReportGetRequest(
        user_id="some example string",
        consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
        client_report_id="some example string",
        report_type=CraCreditProfileReportType.QUALIFY,
        inquiry_type=CraCreditProfileInquiryType.SOFT_INQUIRY,
        version=CraCreditProfileReportVersion.V1,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraCreditProfileReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraCreditProfileReportGetRequest](the_plaid_api/models/cra_credit_profile_report_get_request.py) \| [CraCreditProfileReportGetRequestDict](the_plaid_api/models/cra_credit_profile_report_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraCreditProfileReportGetResponse](the_plaid_api/models/cra_credit_profile_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraCreditProfileReportGetResponse](the_plaid_api/models/cra_credit_profile_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_applications_register(body: CraLoansApplicationsRegisterRequest | CraLoansApplicationsRegisterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraLoansApplicationsRegisterResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/loans/applications/register` registers loan applications and decisions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_loans_applications_register(
    CraLoansApplicationsRegisterRequest(
        applications=[
            CraLoanApplication(
                user_token="some example string",
                application_id="some example string",
                type_=CraLoanType.PERSONAL,
                decision=CraLoanApplicationDecision.APPROVED,
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoansApplicationsRegisterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_loans_applications_register(
    CraLoansApplicationsRegisterRequest(
        applications=[
            CraLoanApplication(
                user_token="some example string",
                application_id="some example string",
                type_=CraLoanType.PERSONAL,
                decision=CraLoanApplicationDecision.APPROVED,
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoansApplicationsRegisterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraLoansApplicationsRegisterRequest](the_plaid_api/models/cra_loans_applications_register_request.py) \| [CraLoansApplicationsRegisterRequestDict](the_plaid_api/models/cra_loans_applications_register_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraLoansApplicationsRegisterResponse](the_plaid_api/models/cra_loans_applications_register_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraLoansApplicationsRegisterResponse](the_plaid_api/models/cra_loans_applications_register_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_register(body: CraloansRegisterRequest | CraloansRegisterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraLoansRegisterResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/loans/register` registers a list of loans to their applicants.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_loans_register(
    CraloansRegisterRequest(
        loans=[
            CraLoanRegister(
                user_token="some example string",
                loan_id="some example string",
                type_=CraLoanType.PERSONAL,
                payment_schedule=CraLoanPaymentSchedule.DAILY,
                opened_date=date(2024, 1, 15),
                opened_with_status=CraLoanOpenedStatus(status=CraLoanStatus.APPROVED, date=date(2024, 1, 15)),
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoansRegisterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_loans_register(
    CraloansRegisterRequest(
        loans=[
            CraLoanRegister(
                user_token="some example string",
                loan_id="some example string",
                type_=CraLoanType.PERSONAL,
                payment_schedule=CraLoanPaymentSchedule.DAILY,
                opened_date=date(2024, 1, 15),
                opened_with_status=CraLoanOpenedStatus(status=CraLoanStatus.APPROVED, date=date(2024, 1, 15)),
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoansRegisterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraloansRegisterRequest](the_plaid_api/models/craloans_register_request.py) \| [CraloansRegisterRequestDict](the_plaid_api/models/craloans_register_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraLoansRegisterResponse](the_plaid_api/models/cra_loans_register_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraLoansRegisterResponse](the_plaid_api/models/cra_loans_register_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_unregister(body: CraLoansUnregisterRequest | CraLoansUnregisterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraLoanUnregisterResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/loans/unregister` indicates the loans have reached a final status and no further updates are expected.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_loans_unregister(
    CraLoansUnregisterRequest(
        loans=[
            CraLoanUnregister(
                loan_id="some example string",
                closed_with_status=CraLoanClosedStatus(status=CraLoanStatus.APPROVED, date=date(2024, 1, 15)),
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoanUnregisterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_loans_unregister(
    CraLoansUnregisterRequest(
        loans=[
            CraLoanUnregister(
                loan_id="some example string",
                closed_with_status=CraLoanClosedStatus(status=CraLoanStatus.APPROVED, date=date(2024, 1, 15)),
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoanUnregisterResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraLoansUnregisterRequest](the_plaid_api/models/cra_loans_unregister_request.py) \| [CraLoansUnregisterRequestDict](the_plaid_api/models/cra_loans_unregister_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraLoanUnregisterResponse](the_plaid_api/models/cra_loan_unregister_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraLoanUnregisterResponse](the_plaid_api/models/cra_loan_unregister_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_update(body: CraLoansUpdateRequest | CraLoansUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraLoansUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/loans/update` updates loan information such as the status and payment history.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_loans_update(CraLoansUpdateRequest(loans=[CraLoanUpdate()]))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoansUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_loans_update(CraLoansUpdateRequest(loans=[CraLoanUpdate()]))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraLoansUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraLoansUpdateRequest](the_plaid_api/models/cra_loans_update_request.py) \| [CraLoansUpdateRequestDict](the_plaid_api/models/cra_loans_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraLoansUpdateResponse](the_plaid_api/models/cra_loans_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraLoansUpdateResponse](the_plaid_api/models/cra_loans_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_monitoring_insights_get(body: CraMonitoringInsightsGetRequest | CraMonitoringInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraMonitoringInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to retrieve a Cash Flow Updates report by passing in the `user_id` referred to in the webhook you received.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_monitoring_insights_get(
    CraMonitoringInsightsGetRequest(
        consumer_report_permissible_purpose=MonitoringConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraMonitoringInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_monitoring_insights_get(
    CraMonitoringInsightsGetRequest(
        consumer_report_permissible_purpose=MonitoringConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraMonitoringInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraMonitoringInsightsGetRequest](the_plaid_api/models/cra_monitoring_insights_get_request.py) \| [CraMonitoringInsightsGetRequestDict](the_plaid_api/models/cra_monitoring_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraMonitoringInsightsGetResponse](the_plaid_api/models/cra_monitoring_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraMonitoringInsightsGetResponse](the_plaid_api/models/cra_monitoring_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_monitoring_insights_subscribe(body: CraMonitoringInsightsSubscribeRequest | CraMonitoringInsightsSubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraMonitoringInsightsSubscribeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to subscribe to insights for a user's linked CRA Item, which are updated between one and four times per day (best-effort). In the current Cash Flow Updates beta experience, only one Item per user may be subscribed for monitoring updates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_monitoring_insights_subscribe(
    CraMonitoringInsightsSubscribeRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraMonitoringInsightsSubscribeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_monitoring_insights_subscribe(
    CraMonitoringInsightsSubscribeRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraMonitoringInsightsSubscribeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraMonitoringInsightsSubscribeRequest](the_plaid_api/models/cra_monitoring_insights_subscribe_request.py) \| [CraMonitoringInsightsSubscribeRequestDict](the_plaid_api/models/cra_monitoring_insights_subscribe_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraMonitoringInsightsSubscribeResponse](the_plaid_api/models/cra_monitoring_insights_subscribe_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraMonitoringInsightsSubscribeResponse](the_plaid_api/models/cra_monitoring_insights_subscribe_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_monitoring_insights_unsubscribe(body: CraMonitoringInsightsUnsubscribeRequest | CraMonitoringInsightsUnsubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraMonitoringInsightsUnsubscribeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you to unsubscribe from previously subscribed Monitoring Insights.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_monitoring_insights_unsubscribe(
    CraMonitoringInsightsUnsubscribeRequest(subscription_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraMonitoringInsightsUnsubscribeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_monitoring_insights_unsubscribe(
    CraMonitoringInsightsUnsubscribeRequest(subscription_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraMonitoringInsightsUnsubscribeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraMonitoringInsightsUnsubscribeRequest](the_plaid_api/models/cra_monitoring_insights_unsubscribe_request.py) \| [CraMonitoringInsightsUnsubscribeRequestDict](the_plaid_api/models/cra_monitoring_insights_unsubscribe_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraMonitoringInsightsUnsubscribeResponse](the_plaid_api/models/cra_monitoring_insights_unsubscribe_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraMonitoringInsightsUnsubscribeResponse](the_plaid_api/models/cra_monitoring_insights_unsubscribe_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_partner_insights_get(body: CraPartnerInsightsGetRequest | CraPartnerInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraPartnerInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/partner_insights/get` returns cash flow insights for a specified user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_partner_insights_get(
    CraPartnerInsightsGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraPartnerInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_partner_insights_get(
    CraPartnerInsightsGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraPartnerInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraPartnerInsightsGetRequest](the_plaid_api/models/cra_partner_insights_get_request.py) \| [CraPartnerInsightsGetRequestDict](the_plaid_api/models/cra_partner_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraPartnerInsightsGetResponse](the_plaid_api/models/cra_partner_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraPartnerInsightsGetResponse](the_plaid_api/models/cra_partner_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_report_get(body: CraReportGetRequest | CraReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CraReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/cra/report/get` retrieves a CRA Report for a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.cra_report_get(
    CraReportGetRequest(
        user_id="some example string",
        products=[CraReportGetRequestProduct(product=Products.ASSETS, version="some example string")],
        decision_stage=CraReportDecisionStage.PREQUALIFICATION,
        consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.cra_report_get(
    CraReportGetRequest(
        user_id="some example string",
        products=[CraReportGetRequestProduct(product=Products.ASSETS, version="some example string")],
        decision_stage=CraReportDecisionStage.PREQUALIFICATION,
        consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CraReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CraReportGetRequest](the_plaid_api/models/cra_report_get_request.py) \| [CraReportGetRequestDict](the_plaid_api/models/cra_report_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CraReportGetResponse](the_plaid_api/models/cra_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CraReportGetResponse](the_plaid_api/models/cra_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_payment_token(body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationPaymentTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.

The `/payment_initiation/payment/token/create` endpoint is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.create_payment_token(
    PaymentInitiationPaymentTokenCreateRequest(payment_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.create_payment_token(
    PaymentInitiationPaymentTokenCreateRequest(payment_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentTokenCreateRequest](the_plaid_api/models/payment_initiation_payment_token_create_request.py) \| [PaymentInitiationPaymentTokenCreateRequestDict](the_plaid_api/models/payment_initiation_payment_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationPaymentTokenCreateResponse](the_plaid_api/models/payment_initiation_payment_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationPaymentTokenCreateResponse](the_plaid_api/models/payment_initiation_payment_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_asset_report_freddie_mac_get(body: AssetReportFreddieGetRequest | AssetReportFreddieGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportFreddieGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/credit/asset_report/freddie_mac/get` endpoint retrieves the Asset Report in Freddie Mac's JSON format.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_asset_report_freddie_mac_get(
    AssetReportFreddieGetRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportFreddieGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_asset_report_freddie_mac_get(
    AssetReportFreddieGetRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportFreddieGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportFreddieGetRequest](the_plaid_api/models/asset_report_freddie_get_request.py) \| [AssetReportFreddieGetRequestDict](the_plaid_api/models/asset_report_freddie_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportFreddieGetResponse](the_plaid_api/models/asset_report_freddie_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportFreddieGetResponse](the_plaid_api/models/asset_report_freddie_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_audit_copy_token_create(body: CreditAuditCopyTokenCreateRequest | CreditAuditCopyTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditAuditCopyTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Plaid can create an Audit Copy token of an Asset Report and/or Income Report to share with a participating Government-Sponsored Enterprise (GSE) if you participate in Fannie Mae's Day 1 Certainty™ program or utilize Freddie Mac's Loan Product Advisor® (LPA®) Asset and Income Modeler (AIM). An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of `/credit/payroll_income/get`).

Use the `/credit/audit_copy_token/create` endpoint to create an `audit_copy_token` and then pass that token to the GSE who needs access.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_audit_copy_token_create(
    CreditAuditCopyTokenCreateRequest(report_tokens=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditAuditCopyTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_audit_copy_token_create(
    CreditAuditCopyTokenCreateRequest(report_tokens=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditAuditCopyTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditAuditCopyTokenCreateRequest](the_plaid_api/models/credit_audit_copy_token_create_request.py) \| [CreditAuditCopyTokenCreateRequestDict](the_plaid_api/models/credit_audit_copy_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditAuditCopyTokenCreateResponse](the_plaid_api/models/credit_audit_copy_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditAuditCopyTokenCreateResponse](the_plaid_api/models/credit_audit_copy_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_audit_copy_token_update(body: CreditAuditCopyTokenUpdateRequest | CreditAuditCopyTokenUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditAuditCopyTokenUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/credit/audit_copy_token/update` endpoint updates an existing Audit Copy Token by adding the report tokens in the `report_tokens` field to the `audit_copy_token`. If the Audit Copy Token already contains a report of a certain type, it will be replaced with the token provided in the `report_tokens` field.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_audit_copy_token_update(
    CreditAuditCopyTokenUpdateRequest(audit_copy_token="some example string", report_tokens=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditAuditCopyTokenUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_audit_copy_token_update(
    CreditAuditCopyTokenUpdateRequest(audit_copy_token="some example string", report_tokens=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditAuditCopyTokenUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditAuditCopyTokenUpdateRequest](the_plaid_api/models/credit_audit_copy_token_update_request.py) \| [CreditAuditCopyTokenUpdateRequestDict](the_plaid_api/models/credit_audit_copy_token_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditAuditCopyTokenUpdateResponse](the_plaid_api/models/credit_audit_copy_token_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditAuditCopyTokenUpdateResponse](the_plaid_api/models/credit_audit_copy_token_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_employment_get(body: CreditBankEmploymentGetRequest | CreditBankEmploymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditBankEmploymentGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/beta/credit/v1/bank_employment/get` returns the employment report(s) derived from bank transaction data for a specified user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_bank_employment_get(
    CreditBankEmploymentGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankEmploymentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_bank_employment_get(
    CreditBankEmploymentGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankEmploymentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditBankEmploymentGetRequest](the_plaid_api/models/credit_bank_employment_get_request.py) \| [CreditBankEmploymentGetRequestDict](the_plaid_api/models/credit_bank_employment_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditBankEmploymentGetResponse](the_plaid_api/models/credit_bank_employment_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditBankEmploymentGetResponse](the_plaid_api/models/credit_bank_employment_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_get(body: CreditBankIncomeGetRequest | CreditBankIncomeGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditBankIncomeGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/bank_income/get` returns the bank income report(s) for a specified user. A single report corresponds to all institutions linked in a single Link session. To include multiple institutions in a single report, use [Multi-Item Link](https://plaid.com/docs/link/multi-item-link). To return older reports, use the `options.count` field.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_bank_income_get(CreditBankIncomeGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankIncomeGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_bank_income_get(CreditBankIncomeGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankIncomeGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditBankIncomeGetRequest](the_plaid_api/models/credit_bank_income_get_request.py) \| [CreditBankIncomeGetRequestDict](the_plaid_api/models/credit_bank_income_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditBankIncomeGetResponse](the_plaid_api/models/credit_bank_income_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditBankIncomeGetResponse](the_plaid_api/models/credit_bank_income_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_pdf_get(body: CreditBankIncomePdfgetRequest | CreditBankIncomePdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/bank_income/pdf/get` returns the most recent bank income report for a specified user in PDF format.  A single report corresponds to all institutions linked in a single Link session. To include multiple institutions in a single report, use [Multi-Item Link](https://plaid.com/docs/link/multi-item-link).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_bank_income_pdf_get(
    CreditBankIncomePdfgetRequest(user_token="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_bank_income_pdf_get(
    CreditBankIncomePdfgetRequest(user_token="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditBankIncomePdfgetRequest](the_plaid_api/models/credit_bank_income_pdfget_request.py) \| [CreditBankIncomePdfgetRequestDict](the_plaid_api/models/credit_bank_income_pdfget_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_refresh(body: CreditBankIncomeRefreshRequest | CreditBankIncomeRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditBankIncomeRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/bank_income/refresh` is deprecated. The backend implementation was removed (returns an `Unimplemented` error at runtime), and the endpoint is no longer part of the documented API surface. To refresh Bank Income data for an existing user, send the user through Link's update mode so they can confirm their income sources. For a fully backend refresh, migrate to CRA Income Insights and call `/cra/check_report/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_bank_income_refresh(
    CreditBankIncomeRefreshRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankIncomeRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_bank_income_refresh(
    CreditBankIncomeRefreshRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankIncomeRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditBankIncomeRefreshRequest](the_plaid_api/models/credit_bank_income_refresh_request.py) \| [CreditBankIncomeRefreshRequestDict](the_plaid_api/models/credit_bank_income_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditBankIncomeRefreshResponse](the_plaid_api/models/credit_bank_income_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditBankIncomeRefreshResponse](the_plaid_api/models/credit_bank_income_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_webhook_update(body: CreditBankIncomeWebhookUpdateRequest | CreditBankIncomeWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditBankIncomeWebhookUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/bank_income/webhook/update` allows you to subscribe or unsubscribe a user for income webhook notifications. By default, all users start out unsubscribed.

If a user is subscribed, on significant changes to the user's income profile, you will receive a `BANK_INCOME_REFRESH_UPDATE` webhook, prompting you to refresh bank income data for the user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_bank_income_webhook_update(
    CreditBankIncomeWebhookUpdateRequest(user_token="some example string", enable_webhooks=True)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankIncomeWebhookUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_bank_income_webhook_update(
    CreditBankIncomeWebhookUpdateRequest(user_token="some example string", enable_webhooks=True)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankIncomeWebhookUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditBankIncomeWebhookUpdateRequest](the_plaid_api/models/credit_bank_income_webhook_update_request.py) \| [CreditBankIncomeWebhookUpdateRequestDict](the_plaid_api/models/credit_bank_income_webhook_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditBankIncomeWebhookUpdateResponse](the_plaid_api/models/credit_bank_income_webhook_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditBankIncomeWebhookUpdateResponse](the_plaid_api/models/credit_bank_income_webhook_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_statements_uploads_get(body: CreditBankStatementsUploadsGetRequest | CreditBankStatementsUploadsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditBankStatementsUploadsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/bank_statements/uploads/get` returns parsed data from bank statements uploaded by users as part of the Document Income flow. If your account is not enabled for Document Parsing, contact your account manager to request access.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_bank_statements_uploads_get(
    CreditBankStatementsUploadsGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankStatementsUploadsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_bank_statements_uploads_get(
    CreditBankStatementsUploadsGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditBankStatementsUploadsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditBankStatementsUploadsGetRequest](the_plaid_api/models/credit_bank_statements_uploads_get_request.py) \| [CreditBankStatementsUploadsGetRequestDict](the_plaid_api/models/credit_bank_statements_uploads_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditBankStatementsUploadsGetResponse](the_plaid_api/models/credit_bank_statements_uploads_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditBankStatementsUploadsGetResponse](the_plaid_api/models/credit_bank_statements_uploads_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_employment_get(body: CreditEmploymentGetRequest | CreditEmploymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditEmploymentGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/employment/get` returns a list of items with employment information from a user's payroll provider that was verified by an end user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_employment_get(CreditEmploymentGetRequest(user_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditEmploymentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_employment_get(
    CreditEmploymentGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditEmploymentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditEmploymentGetRequest](the_plaid_api/models/credit_employment_get_request.py) \| [CreditEmploymentGetRequestDict](the_plaid_api/models/credit_employment_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditEmploymentGetResponse](the_plaid_api/models/credit_employment_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditEmploymentGetResponse](the_plaid_api/models/credit_employment_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_freddie_mac_reports_get(body: CreditFreddieMacReportsGetRequest | CreditFreddieMacReportsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditFreddieMacReportsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/credit/freddie_mac/reports/get` endpoint retrieves the Verification of Assets and Verification of Employment reports.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_freddie_mac_reports_get(
    CreditFreddieMacReportsGetRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditFreddieMacReportsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_freddie_mac_reports_get(
    CreditFreddieMacReportsGetRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditFreddieMacReportsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditFreddieMacReportsGetRequest](the_plaid_api/models/credit_freddie_mac_reports_get_request.py) \| [CreditFreddieMacReportsGetRequestDict](the_plaid_api/models/credit_freddie_mac_reports_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditFreddieMacReportsGetResponse](the_plaid_api/models/credit_freddie_mac_reports_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditFreddieMacReportsGetResponse](the_plaid_api/models/credit_freddie_mac_reports_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_get(body: CreditPayrollIncomeGetRequest | CreditPayrollIncomeGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditPayrollIncomeGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_payroll_income_get(CreditPayrollIncomeGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_payroll_income_get(CreditPayrollIncomeGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditPayrollIncomeGetRequest](the_plaid_api/models/credit_payroll_income_get_request.py) \| [CreditPayrollIncomeGetRequestDict](the_plaid_api/models/credit_payroll_income_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditPayrollIncomeGetResponse](the_plaid_api/models/credit_payroll_income_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditPayrollIncomeGetResponse](the_plaid_api/models/credit_payroll_income_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_parsing_config_update(body: CreditPayrollIncomeParsingConfigUpdateRequest | CreditPayrollIncomeParsingConfigUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditPayrollIncomeParsingConfigUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/payroll_income/parsing_config/update` updates the parsing configuration for a document income verification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_payroll_income_parsing_config_update(
    CreditPayrollIncomeParsingConfigUpdateRequest(
        user_token="some example string", parsing_config=[IncomeVerificationDocParsingConfig.OCR]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeParsingConfigUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_payroll_income_parsing_config_update(
    CreditPayrollIncomeParsingConfigUpdateRequest(
        user_token="some example string", parsing_config=[IncomeVerificationDocParsingConfig.OCR]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeParsingConfigUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditPayrollIncomeParsingConfigUpdateRequest](the_plaid_api/models/credit_payroll_income_parsing_config_update_request.py) \| [CreditPayrollIncomeParsingConfigUpdateRequestDict](the_plaid_api/models/credit_payroll_income_parsing_config_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditPayrollIncomeParsingConfigUpdateResponse](the_plaid_api/models/credit_payroll_income_parsing_config_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditPayrollIncomeParsingConfigUpdateResponse](the_plaid_api/models/credit_payroll_income_parsing_config_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_precheck(body: CreditPayrollIncomePrecheckRequest | CreditPayrollIncomePrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditPayrollIncomePrecheckResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/payroll_income/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

While all request fields are optional, providing `employer` data will increase the chance of receiving a useful result.

When testing in Sandbox, you can control the results by providing special test values in the `employer` and `access_tokens` fields. `employer_good` and `employer_bad` will result in `HIGH` and `LOW` confidence values, respectively. `employer_multi` will result in a `HIGH` confidence with multiple payroll options. Likewise, `access_good` and `access_bad` will result in `HIGH` and `LOW` confidence values, respectively. Any other value for `employer` and `access_tokens` in Sandbox will result in `UNKNOWN` confidence.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_payroll_income_precheck(CreditPayrollIncomePrecheckRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomePrecheckResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_payroll_income_precheck(CreditPayrollIncomePrecheckRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomePrecheckResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditPayrollIncomePrecheckRequest](the_plaid_api/models/credit_payroll_income_precheck_request.py) \| [CreditPayrollIncomePrecheckRequestDict](the_plaid_api/models/credit_payroll_income_precheck_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditPayrollIncomePrecheckResponse](the_plaid_api/models/credit_payroll_income_precheck_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditPayrollIncomePrecheckResponse](the_plaid_api/models/credit_payroll_income_precheck_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_refresh(body: CreditPayrollIncomeRefreshRequest | CreditPayrollIncomeRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditPayrollIncomeRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/payroll_income/refresh` refreshes a given digital payroll income verification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_payroll_income_refresh(
    CreditPayrollIncomeRefreshRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_payroll_income_refresh(
    CreditPayrollIncomeRefreshRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditPayrollIncomeRefreshRequest](the_plaid_api/models/credit_payroll_income_refresh_request.py) \| [CreditPayrollIncomeRefreshRequestDict](the_plaid_api/models/credit_payroll_income_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditPayrollIncomeRefreshResponse](the_plaid_api/models/credit_payroll_income_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditPayrollIncomeRefreshResponse](the_plaid_api/models/credit_payroll_income_refresh_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_risk_signals_get(body: CreditPayrollIncomeRiskSignalsGetRequest | CreditPayrollIncomeRiskSignalsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditPayrollIncomeRiskSignalsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/payroll_income/risk_signals/get` can be used as part of the Document Income flow to assess a user-uploaded document for signs of potential fraud or tampering. It returns a risk score for each uploaded document that indicates the likelihood of the document being fraudulent, in addition to details on the individual risk signals contributing to the score.

To trigger risk signal generation for an Item, call `/link/token/create` with `parsing_config` set to include `risk_signals`, or call `/credit/payroll_income/parsing_config/update`. Once risk signal generation has been triggered, `/credit/payroll_income/risk_signals/get` can be called at any time after the `INCOME_VERIFICATION_RISK_SIGNALS` webhook has been fired.

`/credit/payroll_income/risk_signals/get` is offered as an add-on to Document Income and is billed separately. To request access to this endpoint, submit a product access request or contact your Plaid account manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_payroll_income_risk_signals_get(CreditPayrollIncomeRiskSignalsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeRiskSignalsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_payroll_income_risk_signals_get(
    CreditPayrollIncomeRiskSignalsGetRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditPayrollIncomeRiskSignalsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditPayrollIncomeRiskSignalsGetRequest](the_plaid_api/models/credit_payroll_income_risk_signals_get_request.py) \| [CreditPayrollIncomeRiskSignalsGetRequestDict](the_plaid_api/models/credit_payroll_income_risk_signals_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditPayrollIncomeRiskSignalsGetResponse](the_plaid_api/models/credit_payroll_income_risk_signals_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditPayrollIncomeRiskSignalsGetResponse](the_plaid_api/models/credit_payroll_income_risk_signals_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_create(body: CreditRelayCreateRequest | CreditRelayCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditRelayCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.

To grant a third party access to an Asset Report, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to your third party. Each third party has its own `secondary_client_id`; for example, `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each third party that needs access to the report on your behalf.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_relay_create(
    CreditRelayCreateRequest(report_tokens=["some example string"], secondary_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditRelayCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_relay_create(
    CreditRelayCreateRequest(report_tokens=["some example string"], secondary_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditRelayCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditRelayCreateRequest](the_plaid_api/models/credit_relay_create_request.py) \| [CreditRelayCreateRequestDict](the_plaid_api/models/credit_relay_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditRelayCreateResponse](the_plaid_api/models/credit_relay_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditRelayCreateResponse](the_plaid_api/models/credit_relay_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_get(body: CreditRelayGetRequest | CreditRelayGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssetReportGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/relay/get` allows third parties to receive a report that was shared with them, using a `relay_token` that was created by the report owner.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_relay_get(
    CreditRelayGetRequest(relay_token="some example string", report_type=ReportType.ASSET)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_relay_get(
    CreditRelayGetRequest(relay_token="some example string", report_type=ReportType.ASSET)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssetReportGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditRelayGetRequest](the_plaid_api/models/credit_relay_get_request.py) \| [CreditRelayGetRequestDict](the_plaid_api/models/credit_relay_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_pdf_get(body: CreditRelayPdfgetRequest | CreditRelayPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/credit/relay/pdf/get` allows third parties to receive a PDF report that was shared with them, using a `relay_token` that was created by the report owner.

The `/credit/relay/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/credit/relay/pdf/get`, you must first create the Asset Report using `/credit/relay/create` and then wait for the https://plaid.com/docs/api/products/assets/#product_ready webhook to fire, indicating that the Report is ready to be retrieved.

The response to `/credit/relay/pdf/get` is the PDF binary data. The `request_id` is returned in the `Plaid-Request-ID` header.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_relay_pdf_get(
    CreditRelayPdfgetRequest(relay_token="some example string", report_type=ReportType.ASSET)
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_relay_pdf_get(
    CreditRelayPdfgetRequest(relay_token="some example string", report_type=ReportType.ASSET)
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditRelayPdfgetRequest](the_plaid_api/models/credit_relay_pdfget_request.py) \| [CreditRelayPdfgetRequestDict](the_plaid_api/models/credit_relay_pdfget_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_refresh(body: CreditRelayRefreshRequest | CreditRelayRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditRelayRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/credit/relay/refresh` endpoint allows third parties to refresh a report that was relayed to them, using a `relay_token` that was created by the report owner. A new report will be created with the original report parameters, but with the most recent data available based on the `days_requested` value of the original report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_relay_refresh(
    CreditRelayRefreshRequest(relay_token="some example string", report_type=ReportType.ASSET)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditRelayRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_relay_refresh(
    CreditRelayRefreshRequest(relay_token="some example string", report_type=ReportType.ASSET)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditRelayRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditRelayRefreshRequest](the_plaid_api/models/credit_relay_refresh_request.py) \| [CreditRelayRefreshRequestDict](the_plaid_api/models/credit_relay_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditRelayRefreshResponse](the_plaid_api/models/credit_relay_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditRelayRefreshResponse](the_plaid_api/models/credit_relay_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_remove(body: CreditRelayRemoveRequest | CreditRelayRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditRelayRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`. The third party holding the token will no longer be able to access or refresh the reports which the `relay_token` gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_relay_remove(CreditRelayRemoveRequest(relay_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditRelayRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_relay_remove(
    CreditRelayRemoveRequest(relay_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditRelayRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditRelayRemoveRequest](the_plaid_api/models/credit_relay_remove_request.py) \| [CreditRelayRemoveRequestDict](the_plaid_api/models/credit_relay_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditRelayRemoveResponse](the_plaid_api/models/credit_relay_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditRelayRemoveResponse](the_plaid_api/models/credit_relay_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_report_audit_copy_remove(body: CreditAuditCopyTokenRemoveRequest | CreditAuditCopyTokenRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditAuditCopyTokenRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/credit/audit_copy_token/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_report_audit_copy_remove(
    CreditAuditCopyTokenRemoveRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditAuditCopyTokenRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_report_audit_copy_remove(
    CreditAuditCopyTokenRemoveRequest(audit_copy_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditAuditCopyTokenRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditAuditCopyTokenRemoveRequest](the_plaid_api/models/credit_audit_copy_token_remove_request.py) \| [CreditAuditCopyTokenRemoveRequestDict](the_plaid_api/models/credit_audit_copy_token_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditAuditCopyTokenRemoveResponse](the_plaid_api/models/credit_audit_copy_token_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditAuditCopyTokenRemoveResponse](the_plaid_api/models/credit_audit_copy_token_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_sessions_get(body: CreditSessionsGetRequest | CreditSessionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreditSessionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint can be used for your end users after they complete the Link flow. This endpoint returns a list of Link sessions that your user completed, where each session includes the results from the Link flow.

These results include details about the Item that was created and some product related metadata (showing, for example, whether the user finished the bank income verification step).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.credit_sessions_get(CreditSessionsGetRequest(user_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditSessionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.credit_sessions_get(
    CreditSessionsGetRequest(user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreditSessionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreditSessionsGetRequest](the_plaid_api/models/credit_sessions_get_request.py) \| [CreditSessionsGetRequestDict](the_plaid_api/models/credit_sessions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[CreditSessionsGetResponse](the_plaid_api/models/credit_sessions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreditSessionsGetResponse](the_plaid_api/models/credit_sessions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dashboard_user_get(body: DashboardUserGetRequest | DashboardUserGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DashboardUserGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/dashboard_user/get` endpoint provides details (such as email address) about a specific Dashboard user based on the `dashboard_user_id` field, which is returned in the `audit_trail` object of certain Monitor and Beacon endpoints. This can be used to identify the specific reviewer who performed a Dashboard action.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.dashboard_user_get(DashboardUserGetRequest(dashboard_user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DashboardUserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.dashboard_user_get(
    DashboardUserGetRequest(dashboard_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DashboardUserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DashboardUserGetRequest](the_plaid_api/models/dashboard_user_get_request.py) \| [DashboardUserGetRequestDict](the_plaid_api/models/dashboard_user_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[DashboardUserGetResponse](the_plaid_api/models/dashboard_user_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DashboardUserGetResponse](the_plaid_api/models/dashboard_user_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dashboard_user_list(body: DashboardUserListRequest | DashboardUserListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DashboardUserListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/dashboard_user/list` endpoint provides details (such as email address) about all Dashboard users associated with your account. This can be used to audit or track the list of reviewers for Monitor, Beacon, and Identity Verification products.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.dashboard_user_list(DashboardUserListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DashboardUserListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.dashboard_user_list(DashboardUserListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DashboardUserListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DashboardUserListRequest](the_plaid_api/models/dashboard_user_list_request.py) \| [DashboardUserListRequestDict](the_plaid_api/models/dashboard_user_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[DashboardUserListResponse](the_plaid_api/models/dashboard_user_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DashboardUserListResponse](the_plaid_api/models/dashboard_user_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def employers_search(body: EmployersSearchRequest | EmployersSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EmployersSearchResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/employers/search` allows you the ability to search Plaid's database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.employers_search(
    EmployersSearchRequest(query="some example string", products=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmployersSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.employers_search(
    EmployersSearchRequest(query="some example string", products=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmployersSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[EmployersSearchRequest](the_plaid_api/models/employers_search_request.py) \| [EmployersSearchRequestDict](the_plaid_api/models/employers_search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[EmployersSearchResponse](the_plaid_api/models/employers_search_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EmployersSearchResponse](the_plaid_api/models/employers_search_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def employment_verification_get(body: EmploymentVerificationGetRequest | EmploymentVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EmploymentVerificationGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/employment/verification/get` returns a list of employments through a user payroll that was verified by an end user.

This endpoint has been deprecated; new integrations should use `/credit/employment/get` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.employment_verification_get(
    EmploymentVerificationGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmploymentVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.employment_verification_get(
    EmploymentVerificationGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmploymentVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[EmploymentVerificationGetRequest](the_plaid_api/models/employment_verification_get_request.py) \| [EmploymentVerificationGetRequestDict](the_plaid_api/models/employment_verification_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[EmploymentVerificationGetResponse](the_plaid_api/models/employment_verification_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EmploymentVerificationGetResponse](the_plaid_api/models/employment_verification_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_get(consent_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FdxconsentGrant, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a consent grant by its identifier

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.fdx_consents_get("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FdxconsentGrant
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.fdx_consents_get("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FdxconsentGrant
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>consent_id</code> | <code>str</code> | Consent Grant Identifier. Uniquely identifies the consent grant |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[FdxconsentGrant](the_plaid_api/models/fdxconsent_grant.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FdxconsentGrant](the_plaid_api/models/fdxconsent_grant.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_list(customer_id: str, *, status: FdxConsentGrantStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetConsentsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns zero or more consent grants associated with the given data provider customer, optionally filtered by status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.fdx_consents_list("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetConsentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.fdx_consents_list("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetConsentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | Data provider customer identifier whose consent grants to return. |
| <code>status</code> | <code>[FdxConsentGrantStatusOrStr](the_plaid_api/models/enums/fdx_consent_grant_status.py) \| None</code> | Optional filter restricting results to a single consent grant status. One of `ACTIVE`, `REVOKED`, `EXPIRED`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[GetConsentsResponse](the_plaid_api/models/get_consents_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetConsentsResponse](the_plaid_api/models/get_consents_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_revocation_get(consent_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FdxconsentRevocations, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the revocation history of a consent grant

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.fdx_consents_revocation_get("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FdxconsentRevocations
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.fdx_consents_revocation_get("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FdxconsentRevocations
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>consent_id</code> | <code>str</code> | Consent Grant Identifier. Uniquely identifies the consent grant |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[FdxconsentRevocations](the_plaid_api/models/fdxconsent_revocations.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FdxconsentRevocations](the_plaid_api/models/fdxconsent_revocations.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_revoke(consent_id: str, body: FdxconsentRevocation | FdxconsentRevocationDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Appends a REVOKED status record to the named consent grant

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.fdx_consents_revoke(
    "some example string",
    FdxconsentRevocation(initiator=PartyType.DATA_ACCESS_PLATFORM, reason=FdxUpdateReason.BUSINESS_RULE),
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.fdx_consents_revoke(
    "some example string",
    FdxconsentRevocation(initiator=PartyType.DATA_ACCESS_PLATFORM, reason=FdxUpdateReason.BUSINESS_RULE),
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>consent_id</code> | <code>str</code> | Consent Grant Identifier. Uniquely identifies the consent grant |
| <code>body</code> | <code>[FdxconsentRevocation](the_plaid_api/models/fdxconsent_revocation.py) \| [FdxconsentRevocationDict](the_plaid_api/models/fdxconsent_revocation.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_notifications(body: FdxNotificationEntity | FdxNotificationEntityDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

A generic webhook receiver endpoint for FDX Event Notifications

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.fdx_notifications(
    FdxNotificationEntity(
        notification_id="some example string",
        type_=NotificationType.ACCOUNT_TAKEOVER,
        sent_on=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
        category=NotificationCategory.SECURITY,
        notification_payload=NotificationPayloadEntity(),
    ),
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.fdx_notifications(
    FdxNotificationEntity(
        notification_id="some example string",
        type_=NotificationType.ACCOUNT_TAKEOVER,
        sent_on=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
        category=NotificationCategory.SECURITY,
        notification_payload=NotificationPayloadEntity(),
    ),
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FdxNotificationEntity](the_plaid_api/models/fdx_notification_entity.py) \| [FdxNotificationEntityDict](the_plaid_api/models/fdx_notification_entity.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recipient(recipient_id: str, *, oauth_state_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FdxrecipientMetadata, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a specific recipient

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_recipient("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FdxrecipientMetadata
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.get_recipient("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FdxrecipientMetadata
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>recipient_id</code> | <code>str</code> | Recipient Identifier. Uniquely identifies the recipient |
| <code>oauth_state_id</code> | <code>str \| None</code> | The value that is passed into the OAuth URI 'state' query parameter.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[FdxrecipientMetadata](the_plaid_api/models/fdxrecipient_metadata.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FdxrecipientMetadata](the_plaid_api/models/fdxrecipient_metadata.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recipients(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetRecipientsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of Recipients

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_recipients()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetRecipientsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.get_recipients()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetRecipientsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[GetRecipientsResponse](the_plaid_api/models/get_recipients_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetRecipientsResponse](the_plaid_api/models/get_recipients_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_documents_uploads_get(body: IdentityDocumentsUploadsGetRequest | IdentityDocumentsUploadsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityDocumentsUploadsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/identity/documents/uploads/get` to retrieve identity details when using [Identity Document Upload](https://plaid.com/docs/identity/identity-document-upload/).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_documents_uploads_get(
    IdentityDocumentsUploadsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityDocumentsUploadsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_documents_uploads_get(
    IdentityDocumentsUploadsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityDocumentsUploadsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityDocumentsUploadsGetRequest](the_plaid_api/models/identity_documents_uploads_get_request.py) \| [IdentityDocumentsUploadsGetRequestDict](the_plaid_api/models/identity_documents_uploads_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityDocumentsUploadsGetResponse](the_plaid_api/models/identity_documents_uploads_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityDocumentsUploadsGetResponse](the_plaid_api/models/identity_documents_uploads_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_get(body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.

Note: In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_get(IdentityGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_get(IdentityGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityGetRequest](the_plaid_api/models/identity_get_request.py) \| [IdentityGetRequestDict](the_plaid_api/models/identity_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityGetResponse](the_plaid_api/models/identity_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityGetResponse](the_plaid_api/models/identity_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_match(body: IdentityMatchRequest | IdentityMatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityMatchResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.

Fields within the `balances` object will always be null when retrieved by `/identity/match`. Instead, use the free `/accounts/get` endpoint to request balance cached data, or `/accounts/balance/get` or `/signal/evaluate` for real-time data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_match(IdentityMatchRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityMatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_match(IdentityMatchRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityMatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityMatchRequest](the_plaid_api/models/identity_match_request.py) \| [IdentityMatchRequestDict](the_plaid_api/models/identity_match_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityMatchResponse](the_plaid_api/models/identity_match_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityMatchResponse](the_plaid_api/models/identity_match_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_refresh(body: IdentityRefreshRequest | IdentityRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/identity/refresh` is an optional endpoint for users of the Identity product. It initiates an on-demand extraction to fetch the most up to date Identity information from the Financial Institution. This on-demand extraction takes place in addition to the periodic extractions that automatically occur for any Identity-enabled Item. If changes to Identity are discovered after calling `/identity/refresh`, Plaid will fire a webhook https://plaid.com/docs/api/products/identity/#default_update.

As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints (typically less than 10 seconds, but occasionally up to 30 seconds or more); if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

`/identity/refresh` is offered as an add-on to Identity and has a separate [fee model](https://plaid.com/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_refresh(IdentityRefreshRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_refresh(
    IdentityRefreshRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityRefreshRequest](the_plaid_api/models/identity_refresh_request.py) \| [IdentityRefreshRequestDict](the_plaid_api/models/identity_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityRefreshResponse](the_plaid_api/models/identity_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityRefreshResponse](the_plaid_api/models/identity_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_autofill_create(body: IdentityVerificationAutofillCreateRequest | IdentityVerificationAutofillCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityVerificationAutofillCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Try to autofill an Identity Verification based on the provided phone number, date of birth and country of residence.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_verification_autofill_create(
    IdentityVerificationAutofillCreateRequest(identity_verification_id="flwses_42cF1MNo42r9Xj")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationAutofillCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_verification_autofill_create(
    IdentityVerificationAutofillCreateRequest(identity_verification_id="flwses_42cF1MNo42r9Xj")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationAutofillCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityVerificationAutofillCreateRequest](the_plaid_api/models/identity_verification_autofill_create_request.py) \| [IdentityVerificationAutofillCreateRequestDict](the_plaid_api/models/identity_verification_autofill_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityVerificationAutofillCreateResponse](the_plaid_api/models/identity_verification_autofill_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityVerificationAutofillCreateResponse](the_plaid_api/models/identity_verification_autofill_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_create(body: IdentityVerificationCreateRequest | IdentityVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityVerificationCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new Identity Verification for the user specified by the `client_user_id` and/or `user_id` field. At least one of these two fields must be provided. The requirements and behavior of the verification are determined by the `template_id` provided. If `user_id` is provided, there must be an associated user; otherwise, an error will be returned.

If you don't know whether an active Identity Verification exists for a given `client_user_id` and/or `user_id`, you can specify `"is_idempotent": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and/or `user_id`, and `template_id`. If an Identity Verification is found, it will be returned unmodified with a `200 OK` HTTP status code.


If `user_id` is not provided, you can also use this endpoint to supply information you already have collected about the user; if any of these fields are specified, the screens prompting the user to enter them will be skipped during the Link flow. If `user_id` is provided, user information can not be included in the request body. Please use the `/user/update` endpoint to update user data instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_verification_create(
    IdentityVerificationCreateRequest(is_shareable=True, template_id="some example string", gave_consent=True)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_verification_create(
    IdentityVerificationCreateRequest(is_shareable=True, template_id="some example string", gave_consent=True)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityVerificationCreateRequest](the_plaid_api/models/identity_verification_create_request.py) \| [IdentityVerificationCreateRequestDict](the_plaid_api/models/identity_verification_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityVerificationCreateResponse](the_plaid_api/models/identity_verification_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityVerificationCreateResponse](the_plaid_api/models/identity_verification_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_get(body: IdentityVerificationGetRequest | IdentityVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityVerificationGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a previously created Identity Verification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_verification_get(
    IdentityVerificationGetRequest(identity_verification_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_verification_get(
    IdentityVerificationGetRequest(identity_verification_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityVerificationGetRequest](the_plaid_api/models/identity_verification_get_request.py) \| [IdentityVerificationGetRequestDict](the_plaid_api/models/identity_verification_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityVerificationGetResponse](the_plaid_api/models/identity_verification_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityVerificationGetResponse](the_plaid_api/models/identity_verification_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_list(body: IdentityVerificationListRequest | IdentityVerificationListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityVerificationListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Filter and list Identity Verifications created by your account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_verification_list(
    IdentityVerificationListRequest(template_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_verification_list(
    IdentityVerificationListRequest(template_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityVerificationListRequest](the_plaid_api/models/identity_verification_list_request.py) \| [IdentityVerificationListRequestDict](the_plaid_api/models/identity_verification_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityVerificationListResponse](the_plaid_api/models/identity_verification_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityVerificationListResponse](the_plaid_api/models/identity_verification_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_retry(body: IdentityVerificationRetryRequest | IdentityVerificationRetryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IdentityVerificationRetryResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allow a customer to retry their Identity Verification

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.identity_verification_retry(
    IdentityVerificationRetryRequest(
        client_user_id="some example string", template_id="some example string", strategy=Strategy.RESET
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationRetryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.identity_verification_retry(
    IdentityVerificationRetryRequest(
        client_user_id="some example string", template_id="some example string", strategy=Strategy.RESET
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IdentityVerificationRetryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityVerificationRetryRequest](the_plaid_api/models/identity_verification_retry_request.py) \| [IdentityVerificationRetryRequestDict](the_plaid_api/models/identity_verification_retry_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IdentityVerificationRetryResponse](the_plaid_api/models/identity_verification_retry_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IdentityVerificationRetryResponse](the_plaid_api/models/identity_verification_retry_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_create(body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IncomeVerificationCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.income_verification_create(
    IncomeVerificationCreateRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.income_verification_create(
    IncomeVerificationCreateRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationCreateRequest](the_plaid_api/models/income_verification_create_request.py) \| [IncomeVerificationCreateRequestDict](the_plaid_api/models/income_verification_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IncomeVerificationCreateResponse](the_plaid_api/models/income_verification_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IncomeVerificationCreateResponse](the_plaid_api/models/income_verification_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_documents_download(body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/documents/download` provides the ability to download the source documents associated with the verification.

If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available for download from the payroll provider will be available from this endpoint.

The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be contained in this file.
If not, the response will contain all documents associated with the verification.

The `request_id` is returned in the `Plaid-Request-ID` header.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.income_verification_documents_download(IncomeVerificationDocumentsDownloadRequest())
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.income_verification_documents_download(
    IncomeVerificationDocumentsDownloadRequest()
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationDocumentsDownloadRequest](the_plaid_api/models/income_verification_documents_download_request.py) \| [IncomeVerificationDocumentsDownloadRequestDict](the_plaid_api/models/income_verification_documents_download_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_paystubs_get(body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IncomeVerificationPaystubsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.income_verification_paystubs_get(IncomeVerificationPaystubsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationPaystubsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.income_verification_paystubs_get(IncomeVerificationPaystubsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationPaystubsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationPaystubsGetRequest](the_plaid_api/models/income_verification_paystubs_get_request.py) \| [IncomeVerificationPaystubsGetRequestDict](the_plaid_api/models/income_verification_paystubs_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IncomeVerificationPaystubsGetResponse](the_plaid_api/models/income_verification_paystubs_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IncomeVerificationPaystubsGetResponse](the_plaid_api/models/income_verification_paystubs_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_precheck(body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IncomeVerificationPrecheckResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the `precheck_id` can still be provided to `/link/token/create` and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

While all request fields are optional, providing either `employer` or `transactions_access_tokens` data will increase the chance of receiving a useful result.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/precheck` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.income_verification_precheck(IncomeVerificationPrecheckRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationPrecheckResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.income_verification_precheck(IncomeVerificationPrecheckRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationPrecheckResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationPrecheckRequest](the_plaid_api/models/income_verification_precheck_request.py) \| [IncomeVerificationPrecheckRequestDict](the_plaid_api/models/income_verification_precheck_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IncomeVerificationPrecheckResponse](the_plaid_api/models/income_verification_precheck_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IncomeVerificationPrecheckResponse](the_plaid_api/models/income_verification_precheck_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_taxforms_get(body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IncomeVerificationTaxformsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.income_verification_taxforms_get(IncomeVerificationTaxformsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationTaxformsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.income_verification_taxforms_get(IncomeVerificationTaxformsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IncomeVerificationTaxformsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationTaxformsGetRequest](the_plaid_api/models/income_verification_taxforms_get_request.py) \| [IncomeVerificationTaxformsGetRequestDict](the_plaid_api/models/income_verification_taxforms_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IncomeVerificationTaxformsGetResponse](the_plaid_api/models/income_verification_taxforms_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IncomeVerificationTaxformsGetResponse](the_plaid_api/models/income_verification_taxforms_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_get(body: InstitutionsGetRequest | InstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InstitutionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.

If there is no overlap between an institution's enabled products and a client's enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.institutions_get(
    InstitutionsGetRequest(count=1, offset=1, country_codes=[CountryCode.US])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.institutions_get(
    InstitutionsGetRequest(count=1, offset=1, country_codes=[CountryCode.US])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InstitutionsGetRequest](the_plaid_api/models/institutions_get_request.py) \| [InstitutionsGetRequestDict](the_plaid_api/models/institutions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[InstitutionsGetResponse](the_plaid_api/models/institutions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InstitutionsGetResponse](the_plaid_api/models/institutions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_get_by_id(body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InstitutionsGetByIdResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` to authenticate to this endpoint. The `public_key` has been deprecated; all customers are encouraged to use `client_id` and `secret` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.institutions_get_by_id(
    InstitutionsGetByIdRequest(institution_id="some example string", country_codes=[CountryCode.US])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionsGetByIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.institutions_get_by_id(
    InstitutionsGetByIdRequest(institution_id="some example string", country_codes=[CountryCode.US])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionsGetByIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InstitutionsGetByIdRequest](the_plaid_api/models/institutions_get_by_id_request.py) \| [InstitutionsGetByIdRequestDict](the_plaid_api/models/institutions_get_by_id_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[InstitutionsGetByIdResponse](the_plaid_api/models/institutions_get_by_id_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InstitutionsGetByIdResponse](the_plaid_api/models/institutions_get_by_id_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_search(body: InstitutionsSearchRequest | InstitutionsSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InstitutionsSearchResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.

Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` parameters to authenticate to this endpoint. The `public_key` parameter has since been deprecated; all customers are encouraged to use `client_id` and `secret` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.institutions_search(
    InstitutionsSearchRequest(query="some example string", country_codes=[CountryCode.US])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionsSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.institutions_search(
    InstitutionsSearchRequest(query="some example string", country_codes=[CountryCode.US])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionsSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InstitutionsSearchRequest](the_plaid_api/models/institutions_search_request.py) \| [InstitutionsSearchRequestDict](the_plaid_api/models/institutions_search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[InstitutionsSearchResponse](the_plaid_api/models/institutions_search_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InstitutionsSearchResponse](the_plaid_api/models/institutions_search_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_auth_get(body: InvestmentsAuthGetRequest | InvestmentsAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InvestmentsAuthGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/investments/auth/get` endpoint allows developers to receive user-authorized data to facilitate the transfer of holdings

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.investments_auth_get(InvestmentsAuthGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsAuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.investments_auth_get(
    InvestmentsAuthGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsAuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InvestmentsAuthGetRequest](the_plaid_api/models/investments_auth_get_request.py) \| [InvestmentsAuthGetRequestDict](the_plaid_api/models/investments_auth_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[InvestmentsAuthGetResponse](the_plaid_api/models/investments_auth_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InvestmentsAuthGetResponse](the_plaid_api/models/investments_auth_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_holdings_get(body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InvestmentsHoldingsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.investments_holdings_get(
    InvestmentsHoldingsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsHoldingsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.investments_holdings_get(
    InvestmentsHoldingsGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsHoldingsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InvestmentsHoldingsGetRequest](the_plaid_api/models/investments_holdings_get_request.py) \| [InvestmentsHoldingsGetRequestDict](the_plaid_api/models/investments_holdings_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[InvestmentsHoldingsGetResponse](the_plaid_api/models/investments_holdings_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InvestmentsHoldingsGetResponse](the_plaid_api/models/investments_holdings_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_refresh(body: InvestmentsRefreshRequest | InvestmentsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InvestmentsRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/investments/refresh` is an optional endpoint for users of the Investments product. It initiates an on-demand extraction to fetch the newest investment holdings and transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur one or more times per day for any Investments-enabled Item. If changes to investments are discovered after calling `/investments/refresh`, Plaid will fire webhooks: https://plaid.com/docs/api/products/investments/#holdings-default_update if any new holdings are detected, and https://plaid.com/docs/api/products/investments/#investments_transactions-default_update if any new investment transactions are detected. This webhook will typically not fire in the Sandbox environment, due to the lack of dynamic investment transactions and holdings data. To test this webhook in Sandbox, call `/sandbox/item/fire_webhook`. Updated holdings and investment transactions can be fetched by calling `/investments/holdings/get` and `/investments/transactions/get`. Note that the `/investments/refresh` endpoint is not supported by all institutions. If called on an Item from an institution that does not support this functionality, it will return a `PRODUCT_NOT_SUPPORTED` error.

As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints (typically less than 10 seconds, but occasionally up to 30 seconds or more); if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

`/investments/refresh` is offered as an add-on to Investments and has a separate [fee model](https://plaid.com/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.investments_refresh(InvestmentsRefreshRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.investments_refresh(
    InvestmentsRefreshRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InvestmentsRefreshRequest](the_plaid_api/models/investments_refresh_request.py) \| [InvestmentsRefreshRequestDict](the_plaid_api/models/investments_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[InvestmentsRefreshResponse](the_plaid_api/models/investments_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InvestmentsRefreshResponse](the_plaid_api/models/investments_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_transactions_get(body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InvestmentsTransactionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

Note that Investments does not have a webhook to indicate when initial transaction data has loaded (unless you use the `async_update` option). Instead, if transactions data is not ready when `/investments/transactions/get` is first called, Plaid will wait for the data. For this reason, calling `/investments/transactions/get` immediately after Link may take up to one to two minutes to return.

Data returned by the asynchronous investments extraction flow (when `async_update` is set to true) may not be immediately available to `/investments/transactions/get`. To be alerted when the data is ready to be fetched, listen for the `HISTORICAL_UPDATE` webhook. If no investments history is ready when `/investments/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.investments_transactions_get(
    InvestmentsTransactionsGetRequest(
        access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.investments_transactions_get(
    InvestmentsTransactionsGetRequest(
        access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentsTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InvestmentsTransactionsGetRequest](the_plaid_api/models/investments_transactions_get_request.py) \| [InvestmentsTransactionsGetRequestDict](the_plaid_api/models/investments_transactions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[InvestmentsTransactionsGetResponse](the_plaid_api/models/investments_transactions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InvestmentsTransactionsGetResponse](the_plaid_api/models/investments_transactions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issues_get(body: IssuesGetRequest | IssuesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IssuesGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve detailed information about a specific `Issue`. This endpoint returns a single `Issue` object.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.issues_get(IssuesGetRequest(issue_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IssuesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.issues_get(IssuesGetRequest(issue_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IssuesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IssuesGetRequest](the_plaid_api/models/issues_get_request.py) \| [IssuesGetRequestDict](the_plaid_api/models/issues_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IssuesGetResponse](the_plaid_api/models/issues_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IssuesGetResponse](the_plaid_api/models/issues_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issues_search(body: IssuesSearchRequest | IssuesSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IssuesSearchResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for an issue associated with one of the following identifiers:  `item_id`, `link_session_id` or Link session `request_id`. This endpoint returns a list of `Issue` objects, with an empty list indicating that no issues are associated with the provided identifier. At least one of the identifiers must be provided to perform the search.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.issues_search(IssuesSearchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IssuesSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.issues_search(IssuesSearchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IssuesSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IssuesSearchRequest](the_plaid_api/models/issues_search_request.py) \| [IssuesSearchRequestDict](the_plaid_api/models/issues_search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IssuesSearchResponse](the_plaid_api/models/issues_search_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IssuesSearchResponse](the_plaid_api/models/issues_search_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issues_subscribe(body: IssuesSubscribeRequest | IssuesSubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IssuesSubscribeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows a user to subscribe to updates on a specific `Issue` using a POST method. Subscribers will receive webhook notifications when the issue status changes, particularly when resolved.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.issues_subscribe(
    IssuesSubscribeRequest(issue_id="some example string", webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IssuesSubscribeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.issues_subscribe(
    IssuesSubscribeRequest(issue_id="some example string", webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IssuesSubscribeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IssuesSubscribeRequest](the_plaid_api/models/issues_subscribe_request.py) \| [IssuesSubscribeRequestDict](the_plaid_api/models/issues_subscribe_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[IssuesSubscribeResponse](the_plaid_api/models/issues_subscribe_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IssuesSubscribeResponse](the_plaid_api/models/issues_subscribe_response.py)</code> -- Subscription was successful

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_access_token_invalidate(body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemAccessTokenInvalidateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.

You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_access_token_invalidate(
    ItemAccessTokenInvalidateRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemAccessTokenInvalidateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_access_token_invalidate(
    ItemAccessTokenInvalidateRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemAccessTokenInvalidateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemAccessTokenInvalidateRequest](the_plaid_api/models/item_access_token_invalidate_request.py) \| [ItemAccessTokenInvalidateRequestDict](the_plaid_api/models/item_access_token_invalidate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemAccessTokenInvalidateResponse](the_plaid_api/models/item_access_token_invalidate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemAccessTokenInvalidateResponse](the_plaid_api/models/item_access_token_invalidate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_activity_list(body: ItemActivityListRequest | ItemActivityListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemActivityListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List a historical log of user consent events

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_activity_list(ItemActivityListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemActivityListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_activity_list(ItemActivityListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemActivityListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemActivityListRequest](the_plaid_api/models/item_activity_list_request.py) \| [ItemActivityListRequestDict](the_plaid_api/models/item_activity_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemActivityListResponse](the_plaid_api/models/item_activity_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemActivityListResponse](the_plaid_api/models/item_activity_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_list(body: ItemApplicationListRequest | ItemApplicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemApplicationListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List a user's connected applications

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_application_list(ItemApplicationListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemApplicationListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_application_list(ItemApplicationListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemApplicationListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemApplicationListRequest](the_plaid_api/models/item_application_list_request.py) \| [ItemApplicationListRequestDict](the_plaid_api/models/item_application_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemApplicationListResponse](the_plaid_api/models/item_application_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemApplicationListResponse](the_plaid_api/models/item_application_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_scopes_update(body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemApplicationScopesUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable consumers to update product access on selected accounts for an application.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_application_scopes_update(
    ItemApplicationScopesUpdateRequest(
        access_token="some example string",
        application_id="some example string",
        scopes=Scopes(),
        context=ScopesContext.ENROLLMENT,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemApplicationScopesUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_application_scopes_update(
    ItemApplicationScopesUpdateRequest(
        access_token="some example string",
        application_id="some example string",
        scopes=Scopes(),
        context=ScopesContext.ENROLLMENT,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemApplicationScopesUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemApplicationScopesUpdateRequest](the_plaid_api/models/item_application_scopes_update_request.py) \| [ItemApplicationScopesUpdateRequestDict](the_plaid_api/models/item_application_scopes_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemApplicationScopesUpdateResponse](the_plaid_api/models/item_application_scopes_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemApplicationScopesUpdateResponse](the_plaid_api/models/item_application_scopes_update_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_unlink(body: ItemApplicationUnlinkRequest | ItemApplicationUnlinkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemApplicationUnlinkResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unlink a user's connected application. On an unlink request, Plaid will immediately revoke the Application's access to the User's data.  The User will have to redo the OAuth authentication process in order to restore functionality.

This endpoint only removes ongoing data access permissions, therefore the User will need to reach out to the Application itself in order to disable and delete their account and delete any data that the Application already received (if the Application does not do so by default).

This endpoint should be called in real time as the User is unlinking an Application, and should not be batched in order to ensure that the change is reflected as soon as possible.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_application_unlink(
    ItemApplicationUnlinkRequest(access_token="some example string", application_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemApplicationUnlinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_application_unlink(
    ItemApplicationUnlinkRequest(access_token="some example string", application_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemApplicationUnlinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemApplicationUnlinkRequest](the_plaid_api/models/item_application_unlink_request.py) \| [ItemApplicationUnlinkRequestDict](the_plaid_api/models/item_application_unlink_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemApplicationUnlinkResponse](the_plaid_api/models/item_application_unlink_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemApplicationUnlinkResponse](the_plaid_api/models/item_application_unlink_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_create_public_token(body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemPublicTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).

If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.

A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.

The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_create_public_token(
    ItemPublicTokenCreateRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemPublicTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_create_public_token(
    ItemPublicTokenCreateRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemPublicTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemPublicTokenCreateRequest](the_plaid_api/models/item_public_token_create_request.py) \| [ItemPublicTokenCreateRequestDict](the_plaid_api/models/item_public_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemPublicTokenCreateResponse](the_plaid_api/models/item_public_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemPublicTokenCreateResponse](the_plaid_api/models/item_public_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_get(body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about the status of an Item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_get(ItemGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_get(ItemGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemGetRequest](the_plaid_api/models/item_get_request.py) \| [ItemGetRequestDict](the_plaid_api/models/item_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemGetResponse](the_plaid_api/models/item_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemGetResponse](the_plaid_api/models/item_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_import(body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemImportResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.

Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_import(
    ItemImportRequest(
        products=[Products.ASSETS],
        user_auth=ItemImportRequestUserAuth(user_id="some example string", auth_token="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemImportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_import(
    ItemImportRequest(
        products=[Products.ASSETS],
        user_auth=ItemImportRequestUserAuth(user_id="some example string", auth_token="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemImportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemImportRequest](the_plaid_api/models/item_import_request.py) \| [ItemImportRequestDict](the_plaid_api/models/item_import_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemImportResponse](the_plaid_api/models/item_import_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemImportResponse](the_plaid_api/models/item_import_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_products_terminate(body: ItemProductsTerminateRequest | ItemProductsTerminateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemProductsTerminateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/item/products/terminate` endpoint allows you to terminate an Item. Once terminated, the `access_token` associated with the Item is no longer valid, billing for the Item's products is ended, and relevant webhooks are fired.

`/item/products/terminate` is the recommended way to offboard users or disconnect accounts linked via Plaid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_products_terminate(
    ItemProductsTerminateRequest(
        access_token="some example string", reason_code=ProductsTerminateReasonCode.FRAUD_FIRST_PARTY
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemProductsTerminateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_products_terminate(
    ItemProductsTerminateRequest(
        access_token="some example string", reason_code=ProductsTerminateReasonCode.FRAUD_FIRST_PARTY
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemProductsTerminateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemProductsTerminateRequest](the_plaid_api/models/item_products_terminate_request.py) \| [ItemProductsTerminateRequestDict](the_plaid_api/models/item_products_terminate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemProductsTerminateResponse](the_plaid_api/models/item_products_terminate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemProductsTerminateResponse](the_plaid_api/models/item_products_terminate_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_public_token_exchange(body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemPublicTokenExchangeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.

The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_public_token_exchange(
    ItemPublicTokenExchangeRequest(public_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemPublicTokenExchangeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_public_token_exchange(
    ItemPublicTokenExchangeRequest(public_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemPublicTokenExchangeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemPublicTokenExchangeRequest](the_plaid_api/models/item_public_token_exchange_request.py) \| [ItemPublicTokenExchangeRequestDict](the_plaid_api/models/item_public_token_exchange_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemPublicTokenExchangeResponse](the_plaid_api/models/item_public_token_exchange_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemPublicTokenExchangeResponse](the_plaid_api/models/item_public_token_exchange_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_remove(body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.

Calling `/item/remove` is a recommended best practice when offboarding users or if a user chooses to disconnect an account linked via Plaid. For subscription products, such as Transactions, Liabilities, and Investments, calling `/item/remove` is required to end subscription billing for the Item, unless the end user revoked permission (e.g. via https://my.plaid.com/). For more details, see [Subscription fee model](https://plaid.com/docs/account/billing/#subscription-fee).

On a Trial plan, calling `/item/remove` does not impact the number of remaining Trial Items (bank connections) you have available.

Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove access to them specifically using the `/asset_report/remove` endpoint.

Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.

API versions 2019-05-29 and earlier return a `removed` boolean as part of the response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_remove(ItemRemoveRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_remove(ItemRemoveRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemRemoveRequest](the_plaid_api/models/item_remove_request.py) \| [ItemRemoveRequestDict](the_plaid_api/models/item_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemRemoveResponse](the_plaid_api/models/item_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemRemoveResponse](the_plaid_api/models/item_remove_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_webhook_update(body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemWebhookUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a https://plaid.com/docs/api/items/#webhook_update_acknowledged webhook to the newly specified webhook URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.item_webhook_update(ItemWebhookUpdateRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemWebhookUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.item_webhook_update(
    ItemWebhookUpdateRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemWebhookUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemWebhookUpdateRequest](the_plaid_api/models/item_webhook_update_request.py) \| [ItemWebhookUpdateRequestDict](the_plaid_api/models/item_webhook_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ItemWebhookUpdateResponse](the_plaid_api/models/item_webhook_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemWebhookUpdateResponse](the_plaid_api/models/item_webhook_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def liabilities_get(body: LiabilitiesGetRequest | LiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LiabilitiesGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/link/#linktokencreate).

The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.liabilities_get(LiabilitiesGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LiabilitiesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.liabilities_get(LiabilitiesGetRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LiabilitiesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LiabilitiesGetRequest](the_plaid_api/models/liabilities_get_request.py) \| [LiabilitiesGetRequestDict](the_plaid_api/models/liabilities_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[LiabilitiesGetResponse](the_plaid_api/models/liabilities_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LiabilitiesGetResponse](the_plaid_api/models/liabilities_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_delivery_create(body: LinkDeliveryCreateRequest | LinkDeliveryCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LinkDeliveryCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/link_delivery/create` endpoint to create a Hosted Link session.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.link_delivery_create(LinkDeliveryCreateRequest(link_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkDeliveryCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.link_delivery_create(
    LinkDeliveryCreateRequest(link_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkDeliveryCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LinkDeliveryCreateRequest](the_plaid_api/models/link_delivery_create_request.py) \| [LinkDeliveryCreateRequestDict](the_plaid_api/models/link_delivery_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[LinkDeliveryCreateResponse](the_plaid_api/models/link_delivery_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LinkDeliveryCreateResponse](the_plaid_api/models/link_delivery_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_delivery_get(body: LinkDeliveryGetRequest | LinkDeliveryGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LinkDeliveryGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/link_delivery/get` endpoint to get the status of a Hosted Link session.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.link_delivery_get(
    LinkDeliveryGetRequest(link_delivery_session_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkDeliveryGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.link_delivery_get(
    LinkDeliveryGetRequest(link_delivery_session_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkDeliveryGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LinkDeliveryGetRequest](the_plaid_api/models/link_delivery_get_request.py) \| [LinkDeliveryGetRequestDict](the_plaid_api/models/link_delivery_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[LinkDeliveryGetResponse](the_plaid_api/models/link_delivery_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LinkDeliveryGetResponse](the_plaid_api/models/link_delivery_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_oauth_correlation_id_exchange(body: LinkOauthCorrelationIdExchangeRequest | LinkOauthCorrelationIdExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LinkOauthCorrelationIdExchangeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchange an OAuth `link_correlation_id` for the corresponding `link_token`. The `link_correlation_id` is only available for `payment_initiation` products and is provided to the client via the OAuth `redirect_uri` as a query parameter.
The `link_correlation_id` is ephemeral and expires in a brief period, after which it can no longer be exchanged for the `link_token`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.link_oauth_correlation_id_exchange(
    LinkOauthCorrelationIdExchangeRequest(link_correlation_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkOauthCorrelationIdExchangeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.link_oauth_correlation_id_exchange(
    LinkOauthCorrelationIdExchangeRequest(link_correlation_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkOauthCorrelationIdExchangeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LinkOauthCorrelationIdExchangeRequest](the_plaid_api/models/link_oauth_correlation_id_exchange_request.py) \| [LinkOauthCorrelationIdExchangeRequestDict](the_plaid_api/models/link_oauth_correlation_id_exchange_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[LinkOauthCorrelationIdExchangeResponse](the_plaid_api/models/link_oauth_correlation_id_exchange_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LinkOauthCorrelationIdExchangeResponse](the_plaid_api/models/link_oauth_correlation_id_exchange_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_token_create(body: LinkTokenCreateRequest | LinkTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LinkTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`. For most Plaid products, the `public_token` is saved and exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow. For more details, see the [Link flow overview](https://plaid.com/docs/link/#link-flow-overview).

A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the [update mode](https://plaid.com/docs/link/update-mode) flow for tokens with expired credentials, or the Identity Verification flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.link_token_create(
    LinkTokenCreateRequest(
        client_name="some example string", language="some example string", country_codes=[CountryCode.US]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.link_token_create(
    LinkTokenCreateRequest(
        client_name="some example string", language="some example string", country_codes=[CountryCode.US]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LinkTokenCreateRequest](the_plaid_api/models/link_token_create_request.py) \| [LinkTokenCreateRequestDict](the_plaid_api/models/link_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[LinkTokenCreateResponse](the_plaid_api/models/link_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LinkTokenCreateResponse](the_plaid_api/models/link_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_token_get(body: LinkTokenGetRequest | LinkTokenGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LinkTokenGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/link/token/get` endpoint gets information about a Link session, including all callbacks fired during the session along with their metadata, including the public token. This endpoint is used with Link flows that don't provide a public token via frontend callbacks, such as the [Hosted Link flow](https://plaid.com/docs/link/hosted-link/) and the [Multi-Item Link flow](https://plaid.com/docs/link/multi-item-link/). It also can be useful for debugging purposes.

By default, this endpoint will only return complete event data for Hosted Link sessions. To use `/link/token/get` to retrieve event data for non-Hosted-Link sessions, contact your account manager to request that your account be enabled for Link events. If you do not have an account manager, you can submit this request via a support ticket. Enablement for Link events will also cause you to receive additional webhooks related to Link events, such as the `SESSION_FINISHED` and `EVENTS` webhook.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.link_token_get(LinkTokenGetRequest(link_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkTokenGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.link_token_get(LinkTokenGetRequest(link_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkTokenGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LinkTokenGetRequest](the_plaid_api/models/link_token_get_request.py) \| [LinkTokenGetRequestDict](the_plaid_api/models/link_token_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[LinkTokenGetResponse](the_plaid_api/models/link_token_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LinkTokenGetResponse](the_plaid_api/models/link_token_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def network_status_get(body: NetworkStatusGetRequest | NetworkStatusGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[NetworkStatusGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/network/status/get` endpoint can be used to check whether Plaid has a matching profile for the user.
This is useful for determining if a user is eligible for a streamlined experience, such as Layer. To access this endpoint, contact your Plaid account manager.

Note: it is strongly recommended to check for Layer eligibility in the frontend. `/network/status/get` should only be used for checking Layer eligibility if a frontend check is not possible for your use case.
For instructions on performing a frontend eligibility check, see the [Layer documentation](https://plaid.com/docs/layer/#integration-overview).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.network_status_get(
    NetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type NetworkStatusGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.network_status_get(
    NetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type NetworkStatusGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[NetworkStatusGetRequest](the_plaid_api/models/network_status_get_request.py) \| [NetworkStatusGetRequestDict](the_plaid_api/models/network_status_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[NetworkStatusGetResponse](the_plaid_api/models/network_status_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[NetworkStatusGetResponse](the_plaid_api/models/network_status_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_introspect(body: OauthIntrospectRequest | OauthIntrospectRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OauthIntrospectResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/oauth/introspect` returns metadata about an access token or refresh token.

Note: This endpoint supports `Content-Type: application/x-www-form-urlencoded` as well as JSON. The fields for the form are equivalent to the fields for JSON and conform to the OAuth 2.0 specification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.oauth_introspect(OauthIntrospectRequest(token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthIntrospectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.oauth_introspect(OauthIntrospectRequest(token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthIntrospectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[OauthIntrospectRequest](the_plaid_api/models/oauth_introspect_request.py) \| [OauthIntrospectRequestDict](the_plaid_api/models/oauth_introspect_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[OauthIntrospectResponse](the_plaid_api/models/oauth_introspect_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[OauthIntrospectResponse](the_plaid_api/models/oauth_introspect_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_revoke(body: OauthRevokeRequest | OauthRevokeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OauthRevokeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/oauth/revoke` revokes an access or refresh token, preventing any further use. If a refresh token is revoked, all access and refresh tokens derived from it are also revoked, including exchanged tokens.

Note: This endpoint supports `Content-Type: application/x-www-form-urlencoded` as well as JSON. The fields for the form are equivalent to the fields for JSON and conform to the OAuth 2.0 specification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.oauth_revoke(OauthRevokeRequest(token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthRevokeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.oauth_revoke(OauthRevokeRequest(token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthRevokeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[OauthRevokeRequest](the_plaid_api/models/oauth_revoke_request.py) \| [OauthRevokeRequestDict](the_plaid_api/models/oauth_revoke_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[OauthRevokeResponse](the_plaid_api/models/oauth_revoke_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[OauthRevokeResponse](the_plaid_api/models/oauth_revoke_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_token(body: OauthTokenRequest | OauthTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OauthTokenResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/oauth/token` issues an access token and refresh token depending on the `grant_type` provided. This endpoint supports `Content-Type: application/x-www-form-urlencoded` as well as JSON. The fields for the form are equivalent to the fields for JSON and conform to the OAuth 2.0 specification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.oauth_token(OauthTokenRequest(grant_type=OauthGrantType.REFRESH_TOKEN))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.oauth_token(OauthTokenRequest(grant_type=OauthGrantType.REFRESH_TOKEN))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[OauthTokenRequest](the_plaid_api/models/oauth_token_request.py) \| [OauthTokenRequestDict](the_plaid_api/models/oauth_token_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[OauthTokenResponse](the_plaid_api/models/oauth_token_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[OauthTokenResponse](the_plaid_api/models/oauth_token_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_create(body: PartnerCustomerCreateRequest | PartnerCustomerCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PartnerCustomerCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/partner/customer/create` endpoint is used by reseller partners to create end customers. To create end customers, it should be called in the Production environment only, even when creating Sandbox API keys. If called in the Sandbox environment, it will return a sample response, but no customer will be created and the API keys will not be valid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.partner_customer_create(
    PartnerCustomerCreateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        company_name="Plaid",
        is_diligence_attested=True,
        products=[Products.AUTH, Products.IDENTITY],
        create_link_customization=True,
        legal_entity_name="Plaid",
        website="plaid.com",
        application_name="Plaid",
        technical_contact=PartnerEndCustomerTechnicalContact(
            given_name="Alice", family_name="Smith", email="alice.smith@example.com"
        ),
        billing_contact=PartnerEndCustomerBillingContact(
            given_name="Bob", family_name="Jones", email="bob.jones@example.com"
        ),
        customer_support_info=PartnerEndCustomerCustomerSupportInfo(
            email="support@example.com",
            phone_number="1234567890",
            contact_url="example.com/contact",
            link_update_url="example.com/update",
        ),
        address=PartnerEndCustomerAddress(
            city="New York", street="123 Main St", region="NY", postal_code="12345", country_code="US"
        ),
        is_bank_addendum_completed=True,
        redirect_uris=["http://localhost/oauth.html", "https://www.example.com/oauth.html"],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.partner_customer_create(
    PartnerCustomerCreateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        company_name="Plaid",
        is_diligence_attested=True,
        products=[Products.AUTH, Products.IDENTITY],
        create_link_customization=True,
        legal_entity_name="Plaid",
        website="plaid.com",
        application_name="Plaid",
        technical_contact=PartnerEndCustomerTechnicalContact(
            given_name="Alice", family_name="Smith", email="alice.smith@example.com"
        ),
        billing_contact=PartnerEndCustomerBillingContact(
            given_name="Bob", family_name="Jones", email="bob.jones@example.com"
        ),
        customer_support_info=PartnerEndCustomerCustomerSupportInfo(
            email="support@example.com",
            phone_number="1234567890",
            contact_url="example.com/contact",
            link_update_url="example.com/update",
        ),
        address=PartnerEndCustomerAddress(
            city="New York", street="123 Main St", region="NY", postal_code="12345", country_code="US"
        ),
        is_bank_addendum_completed=True,
        redirect_uris=["http://localhost/oauth.html", "https://www.example.com/oauth.html"],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PartnerCustomerCreateRequest](the_plaid_api/models/partner_customer_create_request.py) \| [PartnerCustomerCreateRequestDict](the_plaid_api/models/partner_customer_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PartnerCustomerCreateResponse](the_plaid_api/models/partner_customer_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PartnerCustomerCreateResponse](the_plaid_api/models/partner_customer_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_enable(body: PartnerCustomerEnableRequest | PartnerCustomerEnableRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PartnerCustomerEnableResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/partner/customer/enable` endpoint is used by reseller partners to enable an end customer in the full Production environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.partner_customer_enable(
    PartnerCustomerEnableRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerEnableResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.partner_customer_enable(
    PartnerCustomerEnableRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerEnableResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PartnerCustomerEnableRequest](the_plaid_api/models/partner_customer_enable_request.py) \| [PartnerCustomerEnableRequestDict](the_plaid_api/models/partner_customer_enable_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PartnerCustomerEnableResponse](the_plaid_api/models/partner_customer_enable_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PartnerCustomerEnableResponse](the_plaid_api/models/partner_customer_enable_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_get(body: PartnerCustomerGetRequest | PartnerCustomerGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PartnerCustomerGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/partner/customer/get` endpoint is used by reseller partners to retrieve data about a single end customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.partner_customer_get(
    PartnerCustomerGetRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.partner_customer_get(
    PartnerCustomerGetRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PartnerCustomerGetRequest](the_plaid_api/models/partner_customer_get_request.py) \| [PartnerCustomerGetRequestDict](the_plaid_api/models/partner_customer_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PartnerCustomerGetResponse](the_plaid_api/models/partner_customer_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PartnerCustomerGetResponse](the_plaid_api/models/partner_customer_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_oauth_institutions_get(body: PartnerCustomerOauthInstitutionsGetRequest | PartnerCustomerOauthInstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PartnerCustomerOauthInstitutionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/partner/customer/oauth_institutions/get` endpoint is used by reseller partners to retrieve OAuth-institution registration information about a single end customer. To learn how to set up a webhook to listen to status update events, visit the [reseller documentation](https://plaid.com/docs/account/resellers/#enabling-end-customers).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.partner_customer_oauth_institutions_get(
    PartnerCustomerOauthInstitutionsGetRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerOauthInstitutionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.partner_customer_oauth_institutions_get(
    PartnerCustomerOauthInstitutionsGetRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerOauthInstitutionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PartnerCustomerOauthInstitutionsGetRequest](the_plaid_api/models/partner_customer_oauth_institutions_get_request.py) \| [PartnerCustomerOauthInstitutionsGetRequestDict](the_plaid_api/models/partner_customer_oauth_institutions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PartnerCustomerOauthInstitutionsGetResponse](the_plaid_api/models/partner_customer_oauth_institutions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PartnerCustomerOauthInstitutionsGetResponse](the_plaid_api/models/partner_customer_oauth_institutions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_remove(body: PartnerCustomerRemoveRequest | PartnerCustomerRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PartnerCustomerRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/partner/customer/remove` endpoint is used by reseller partners to remove an end customer. Removing an end customer will remove it from view in the Plaid Dashboard and deactivate its API keys. This endpoint can only be used to remove an end customer that has not yet been enabled in full Production.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.partner_customer_remove(
    PartnerCustomerRemoveRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.partner_customer_remove(
    PartnerCustomerRemoveRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        end_customer_client_id="7f57eb3d2a9j6480121fx361",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PartnerCustomerRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PartnerCustomerRemoveRequest](the_plaid_api/models/partner_customer_remove_request.py) \| [PartnerCustomerRemoveRequestDict](the_plaid_api/models/partner_customer_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PartnerCustomerRemoveResponse](the_plaid_api/models/partner_customer_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PartnerCustomerRemoveResponse](the_plaid_api/models/partner_customer_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_create(body: PaymentInitiationConsentCreateRequest | PaymentInitiationConsentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationConsentCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/consent/create` endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with `UNAUTHORISED` status by default and must be authorised by the user before payments can be initiated.

Consents can be limited in time and scope, and have constraints that describe limitations for payments.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_consent_create(
    PaymentInitiationConsentCreateRequest(
        recipient_id="some example string",
        reference="some example string",
        constraints=PaymentInitiationConsentConstraints(
            max_payment_amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
            periodic_amounts=[
                PaymentConsentPeriodicAmount(
                    amount=PaymentAmount(),
                    interval=PaymentConsentPeriodicInterval.DAY,
                    alignment=PaymentConsentPeriodicAlignment.CALENDAR,
                ),
            ],
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_consent_create(
    PaymentInitiationConsentCreateRequest(
        recipient_id="some example string",
        reference="some example string",
        constraints=PaymentInitiationConsentConstraints(
            max_payment_amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
            periodic_amounts=[
                PaymentConsentPeriodicAmount(
                    amount=PaymentAmount(),
                    interval=PaymentConsentPeriodicInterval.DAY,
                    alignment=PaymentConsentPeriodicAlignment.CALENDAR,
                ),
            ],
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationConsentCreateRequest](the_plaid_api/models/payment_initiation_consent_create_request.py) \| [PaymentInitiationConsentCreateRequestDict](the_plaid_api/models/payment_initiation_consent_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationConsentCreateResponse](the_plaid_api/models/payment_initiation_consent_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationConsentCreateResponse](the_plaid_api/models/payment_initiation_consent_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_get(body: PaymentInitiationConsentGetRequest | PaymentInitiationConsentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationConsentGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/consent/get` endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_consent_get(
    PaymentInitiationConsentGetRequest(consent_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_consent_get(
    PaymentInitiationConsentGetRequest(consent_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationConsentGetRequest](the_plaid_api/models/payment_initiation_consent_get_request.py) \| [PaymentInitiationConsentGetRequestDict](the_plaid_api/models/payment_initiation_consent_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationConsentGetResponse](the_plaid_api/models/payment_initiation_consent_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationConsentGetResponse](the_plaid_api/models/payment_initiation_consent_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_payment_execute(body: PaymentInitiationConsentPaymentExecuteRequest | PaymentInitiationConsentPaymentExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationConsentPaymentExecuteResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/consent/payment/execute` endpoint can be used to execute payments using payment consent.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_consent_payment_execute(
    PaymentInitiationConsentPaymentExecuteRequest(
        consent_id="some example string",
        amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
        idempotency_key="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentPaymentExecuteResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_consent_payment_execute(
    PaymentInitiationConsentPaymentExecuteRequest(
        consent_id="some example string",
        amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
        idempotency_key="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentPaymentExecuteResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationConsentPaymentExecuteRequest](the_plaid_api/models/payment_initiation_consent_payment_execute_request.py) \| [PaymentInitiationConsentPaymentExecuteRequestDict](the_plaid_api/models/payment_initiation_consent_payment_execute_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationConsentPaymentExecuteResponse](the_plaid_api/models/payment_initiation_consent_payment_execute_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationConsentPaymentExecuteResponse](the_plaid_api/models/payment_initiation_consent_payment_execute_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_revoke(body: PaymentInitiationConsentRevokeRequest | PaymentInitiationConsentRevokeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationConsentRevokeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/consent/revoke` endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_consent_revoke(
    PaymentInitiationConsentRevokeRequest(consent_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentRevokeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_consent_revoke(
    PaymentInitiationConsentRevokeRequest(consent_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationConsentRevokeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationConsentRevokeRequest](the_plaid_api/models/payment_initiation_consent_revoke_request.py) \| [PaymentInitiationConsentRevokeRequestDict](the_plaid_api/models/payment_initiation_consent_revoke_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationConsentRevokeResponse](the_plaid_api/models/payment_initiation_consent_revoke_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationConsentRevokeResponse](the_plaid_api/models/payment_initiation_consent_revoke_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_create(body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationPaymentCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in EUR, GBP, or another chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency).  If making domestic GBP-denominated payments, your recipient must have been created with Bacs numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer, GBP-denominated payments will be sent via the Faster Payments network and for non-Eurozone markets typically via the local payment scheme, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer or other local payment schemes will typically arrive in one business day.

Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient's account, although at least 90% of standing order payments are sent by 6am.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_payment_create(
    PaymentInitiationPaymentCreateRequest(
        recipient_id="some example string",
        reference="some example string",
        amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_payment_create(
    PaymentInitiationPaymentCreateRequest(
        recipient_id="some example string",
        reference="some example string",
        amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentCreateRequest](the_plaid_api/models/payment_initiation_payment_create_request.py) \| [PaymentInitiationPaymentCreateRequestDict](the_plaid_api/models/payment_initiation_payment_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationPaymentCreateResponse](the_plaid_api/models/payment_initiation_payment_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationPaymentCreateResponse](the_plaid_api/models/payment_initiation_payment_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_get(body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationPaymentGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

Polling for status updates in Production is highly discouraged. Repeatedly calling `/payment_initiation/payment/get` to check a payment's status is unreliable and may trigger API rate limits. Only the `payment_status_update` webhook should be used to receive real-time status updates in Production.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_payment_get(
    PaymentInitiationPaymentGetRequest(payment_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_payment_get(
    PaymentInitiationPaymentGetRequest(payment_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentGetRequest](the_plaid_api/models/payment_initiation_payment_get_request.py) \| [PaymentInitiationPaymentGetRequestDict](the_plaid_api/models/payment_initiation_payment_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationPaymentGetResponse](the_plaid_api/models/payment_initiation_payment_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationPaymentGetResponse](the_plaid_api/models/payment_initiation_payment_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_list(body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationPaymentListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_payment_list(PaymentInitiationPaymentListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_payment_list(PaymentInitiationPaymentListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentListRequest](the_plaid_api/models/payment_initiation_payment_list_request.py) \| [PaymentInitiationPaymentListRequestDict](the_plaid_api/models/payment_initiation_payment_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationPaymentListResponse](the_plaid_api/models/payment_initiation_payment_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationPaymentListResponse](the_plaid_api/models/payment_initiation_payment_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_reverse(body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationPaymentReverseResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reverse a settled payment from a Plaid virtual account.

The original payment must be in a settled state to be refunded.
To refund partially, specify the amount as part of the request.
If the amount is not specified, the refund amount will be equal to all
of the remaining payment amount that has not been refunded yet.

The refund will go back to the source account that initiated the payment.
The original payment must have been initiated to a Plaid virtual account
so that this account can be used to initiate the refund.

Providing counterparty information such as date of birth and address increases
the likelihood of refund being successful without human intervention.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_payment_reverse(
    PaymentInitiationPaymentReverseRequest(
        payment_id="some example string", idempotency_key="some example string", reference="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentReverseResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_payment_reverse(
    PaymentInitiationPaymentReverseRequest(
        payment_id="some example string", idempotency_key="some example string", reference="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationPaymentReverseResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentReverseRequest](the_plaid_api/models/payment_initiation_payment_reverse_request.py) \| [PaymentInitiationPaymentReverseRequestDict](the_plaid_api/models/payment_initiation_payment_reverse_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationPaymentReverseResponse](the_plaid_api/models/payment_initiation_payment_reverse_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationPaymentReverseResponse](the_plaid_api/models/payment_initiation_payment_reverse_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_create(body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationRecipientCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payments Area (SEPA) or a non-Eurozone country [supported](https://support.plaid.com/hc/en-us/articles/27895826947735-What-Plaid-products-are-supported-in-each-country-and-region) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.

It is recommended to use `bacs` in the UK and `iban` in EU.

The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_recipient_create(
    PaymentInitiationRecipientCreateRequest(name="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationRecipientCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_recipient_create(
    PaymentInitiationRecipientCreateRequest(name="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationRecipientCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationRecipientCreateRequest](the_plaid_api/models/payment_initiation_recipient_create_request.py) \| [PaymentInitiationRecipientCreateRequestDict](the_plaid_api/models/payment_initiation_recipient_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationRecipientCreateResponse](the_plaid_api/models/payment_initiation_recipient_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationRecipientCreateResponse](the_plaid_api/models/payment_initiation_recipient_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_get(body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationRecipientGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get details about a payment recipient you have previously created.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_recipient_get(
    PaymentInitiationRecipientGetRequest(recipient_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationRecipientGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_recipient_get(
    PaymentInitiationRecipientGetRequest(recipient_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationRecipientGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationRecipientGetRequest](the_plaid_api/models/payment_initiation_recipient_get_request.py) \| [PaymentInitiationRecipientGetRequestDict](the_plaid_api/models/payment_initiation_recipient_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationRecipientGetResponse](the_plaid_api/models/payment_initiation_recipient_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationRecipientGetResponse](the_plaid_api/models/payment_initiation_recipient_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_list(body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentInitiationRecipientListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/recipient/list` endpoint lists the payment recipients that you have previously created.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_initiation_recipient_list(PaymentInitiationRecipientListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationRecipientListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_initiation_recipient_list(PaymentInitiationRecipientListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentInitiationRecipientListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationRecipientListRequest](the_plaid_api/models/payment_initiation_recipient_list_request.py) \| [PaymentInitiationRecipientListRequestDict](the_plaid_api/models/payment_initiation_recipient_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentInitiationRecipientListResponse](the_plaid_api/models/payment_initiation_recipient_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentInitiationRecipientListResponse](the_plaid_api/models/payment_initiation_recipient_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_profile_create(body: PaymentProfileCreateRequest | PaymentProfileCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentProfileCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/payment_profile/create` endpoint to create a new payment profile.
To initiate the account linking experience, call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field.
You can then use the `payment_profile_token` when creating transfers using `/transfer/authorization/create` and `/transfer/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_profile_create(PaymentProfileCreateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentProfileCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_profile_create(PaymentProfileCreateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentProfileCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentProfileCreateRequest](the_plaid_api/models/payment_profile_create_request.py) \| [PaymentProfileCreateRequestDict](the_plaid_api/models/payment_profile_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentProfileCreateResponse](the_plaid_api/models/payment_profile_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentProfileCreateResponse](the_plaid_api/models/payment_profile_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_profile_get(body: PaymentProfileGetRequest | PaymentProfileGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentProfileGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/payment_profile/get` endpoint to get the status of a given Payment Profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_profile_get(
    PaymentProfileGetRequest(payment_profile_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentProfileGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_profile_get(
    PaymentProfileGetRequest(payment_profile_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentProfileGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentProfileGetRequest](the_plaid_api/models/payment_profile_get_request.py) \| [PaymentProfileGetRequestDict](the_plaid_api/models/payment_profile_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentProfileGetResponse](the_plaid_api/models/payment_profile_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentProfileGetResponse](the_plaid_api/models/payment_profile_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_profile_remove(body: PaymentProfileRemoveRequest | PaymentProfileRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaymentProfileRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/payment_profile/remove` endpoint to remove a given Payment Profile. Once it's removed, it can no longer be used to create transfers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.payment_profile_remove(
    PaymentProfileRemoveRequest(payment_profile_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentProfileRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.payment_profile_remove(
    PaymentProfileRemoveRequest(payment_profile_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaymentProfileRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentProfileRemoveRequest](the_plaid_api/models/payment_profile_remove_request.py) \| [PaymentProfileRemoveRequestDict](the_plaid_api/models/payment_profile_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[PaymentProfileRemoveResponse](the_plaid_api/models/payment_profile_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaymentProfileRemoveResponse](the_plaid_api/models/payment_profile_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_account_get(body: ProcessorAccountGetRequest | ProcessorAccountGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorAccountGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns the account associated with a given processor token.

This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, the account balance returned may not be up-to-date; for real-time balance information, use `/processor/balance/get` instead. Note that some information is nullable.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_account_get(
    ProcessorAccountGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorAccountGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_account_get(
    ProcessorAccountGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorAccountGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorAccountGetRequest](the_plaid_api/models/processor_account_get_request.py) \| [ProcessorAccountGetRequestDict](the_plaid_api/models/processor_account_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorAccountGetResponse](the_plaid_api/models/processor_account_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorAccountGetResponse](the_plaid_api/models/processor_account_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_apex_processor_token_create(body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_apex_processor_token_create(
    ProcessorApexProcessorTokenCreateRequest(access_token="some example string", account_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_apex_processor_token_create(
    ProcessorApexProcessorTokenCreateRequest(access_token="some example string", account_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorApexProcessorTokenCreateRequest](the_plaid_api/models/processor_apex_processor_token_create_request.py) \| [ProcessorApexProcessorTokenCreateRequestDict](the_plaid_api/models/processor_apex_processor_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_auth_get(body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorAuthGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking, savings, or cash management account that''s associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.

Versioning note: API versions 2019-05-29 and earlier use a different schema for the `numbers` object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_auth_get(ProcessorAuthGetRequest(processor_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorAuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_auth_get(
    ProcessorAuthGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorAuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorAuthGetRequest](the_plaid_api/models/processor_auth_get_request.py) \| [ProcessorAuthGetRequestDict](the_plaid_api/models/processor_auth_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorAuthGetResponse](the_plaid_api/models/processor_auth_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorAuthGetResponse](the_plaid_api/models/processor_auth_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_balance_get(body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorBalanceGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_balance_get(
    ProcessorBalanceGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorBalanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_balance_get(
    ProcessorBalanceGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorBalanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorBalanceGetRequest](the_plaid_api/models/processor_balance_get_request.py) \| [ProcessorBalanceGetRequestDict](the_plaid_api/models/processor_balance_get_request.py)</code> | The `/processor/balance/get` endpoint returns the real-time balance for the account associated with a given `processor_token`.<br><br>The current balance is the total amount of funds in the account. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.<br><br>Note that not all institutions calculate the available balance. In the event that available balance is unavailable from the institution, Plaid will return an available balance value of `null`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorBalanceGetResponse](the_plaid_api/models/processor_balance_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorBalanceGetResponse](the_plaid_api/models/processor_balance_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_bank_transfer_create(body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorBankTransferCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_bank_transfer_create(
    ProcessorBankTransferCreateRequest(
        idempotency_key="some example string",
        processor_token="some example string",
        type_=BankTransferType.DEBIT,
        network=BankTransferNetwork.ACH,
        amount="some example string",
        iso_currency_code="some example string",
        description="some example string",
        user=BankTransferUser(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorBankTransferCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_bank_transfer_create(
    ProcessorBankTransferCreateRequest(
        idempotency_key="some example string",
        processor_token="some example string",
        type_=BankTransferType.DEBIT,
        network=BankTransferNetwork.ACH,
        amount="some example string",
        iso_currency_code="some example string",
        description="some example string",
        user=BankTransferUser(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorBankTransferCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorBankTransferCreateRequest](the_plaid_api/models/processor_bank_transfer_create_request.py) \| [ProcessorBankTransferCreateRequestDict](the_plaid_api/models/processor_bank_transfer_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorBankTransferCreateResponse](the_plaid_api/models/processor_bank_transfer_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorBankTransferCreateResponse](the_plaid_api/models/processor_bank_transfer_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_identity_get(body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorIdentityGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_identity_get(
    ProcessorIdentityGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorIdentityGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_identity_get(
    ProcessorIdentityGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorIdentityGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorIdentityGetRequest](the_plaid_api/models/processor_identity_get_request.py) \| [ProcessorIdentityGetRequestDict](the_plaid_api/models/processor_identity_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorIdentityGetResponse](the_plaid_api/models/processor_identity_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorIdentityGetResponse](the_plaid_api/models/processor_identity_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_identity_match(body: ProcessorIdentityMatchRequest | ProcessorIdentityMatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorIdentityMatchResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.

Fields within the `balances` object will always be null when retrieved by `/processor/identity/match`. Instead, use the `/processor/balance/get` endpoint to retrieve balance data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_identity_match(
    ProcessorIdentityMatchRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorIdentityMatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_identity_match(
    ProcessorIdentityMatchRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorIdentityMatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorIdentityMatchRequest](the_plaid_api/models/processor_identity_match_request.py) \| [ProcessorIdentityMatchRequestDict](the_plaid_api/models/processor_identity_match_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorIdentityMatchResponse](the_plaid_api/models/processor_identity_match_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorIdentityMatchResponse](the_plaid_api/models/processor_identity_match_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_investments_auth_get(body: ProcessorInvestmentsAuthGetRequest | ProcessorInvestmentsAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorInvestmentsAuthGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/investments/auth/get` endpoint allows you to retrieve information about the account
authorized by a processor token, including account numbers, account owners, holdings, and data provenance information.

To receive Investments Auth webhooks for a processor token, set its webhook URL via the https://plaid.com/docs/api/processor-partners/#processortokenwebhookupdate endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_investments_auth_get(
    ProcessorInvestmentsAuthGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorInvestmentsAuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_investments_auth_get(
    ProcessorInvestmentsAuthGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorInvestmentsAuthGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorInvestmentsAuthGetRequest](the_plaid_api/models/processor_investments_auth_get_request.py) \| [ProcessorInvestmentsAuthGetRequestDict](the_plaid_api/models/processor_investments_auth_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorInvestmentsAuthGetResponse](the_plaid_api/models/processor_investments_auth_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorInvestmentsAuthGetResponse](the_plaid_api/models/processor_investments_auth_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_investments_holdings_get(body: ProcessorInvestmentsHoldingsGetRequest | ProcessorInvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorInvestmentsHoldingsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns the stock position data of the account associated with a given processor token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_investments_holdings_get(
    ProcessorInvestmentsHoldingsGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorInvestmentsHoldingsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_investments_holdings_get(
    ProcessorInvestmentsHoldingsGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorInvestmentsHoldingsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorInvestmentsHoldingsGetRequest](the_plaid_api/models/processor_investments_holdings_get_request.py) \| [ProcessorInvestmentsHoldingsGetRequestDict](the_plaid_api/models/processor_investments_holdings_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorInvestmentsHoldingsGetResponse](the_plaid_api/models/processor_investments_holdings_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorInvestmentsHoldingsGetResponse](the_plaid_api/models/processor_investments_holdings_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_investments_transactions_get(body: ProcessorInvestmentsTransactionsGetRequest | ProcessorInvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorInvestmentsTransactionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for the investment account associated with the processor token.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

Due to the potentially large number of investment transactions associated with the account, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

Note that Investments does not have a webhook to indicate when initial transaction data has loaded (unless you use the `async_update` option). Instead, if transactions data is not ready when `/processor/investments/transactions/get` is first called, Plaid will wait for the data. For this reason, calling `/processor/investments/transactions/get` immediately after Link may take up to one to two minutes to return.

Data returned by the asynchronous investments extraction flow (when `async_update` is set to true) may not be immediately available to `/processor/investments/transactions/get`. To be alerted when the data is ready to be fetched, listen for the `HISTORICAL_UPDATE` webhook. If no investments history is ready when `/processor/investments/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

To receive Investments Transactions webhooks for a processor token, set its webhook URL via the https://plaid.com/docs/api/processor-partners/#processortokenwebhookupdate endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_investments_transactions_get(
    ProcessorInvestmentsTransactionsGetRequest(
        processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorInvestmentsTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_investments_transactions_get(
    ProcessorInvestmentsTransactionsGetRequest(
        processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorInvestmentsTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorInvestmentsTransactionsGetRequest](the_plaid_api/models/processor_investments_transactions_get_request.py) \| [ProcessorInvestmentsTransactionsGetRequestDict](the_plaid_api/models/processor_investments_transactions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorInvestmentsTransactionsGetResponse](the_plaid_api/models/processor_investments_transactions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorInvestmentsTransactionsGetResponse](the_plaid_api/models/processor_investments_transactions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_liabilities_get(body: ProcessorLiabilitiesGetRequest | ProcessorLiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorLiabilitiesGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/liabilities/get` endpoint returns various details about a loan or credit account. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`.

The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/processor/liabilities/get`.

Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the processor token. This is because Plaid must communicate directly with the institution to retrieve the additional data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_liabilities_get(
    ProcessorLiabilitiesGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorLiabilitiesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_liabilities_get(
    ProcessorLiabilitiesGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorLiabilitiesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorLiabilitiesGetRequest](the_plaid_api/models/processor_liabilities_get_request.py) \| [ProcessorLiabilitiesGetRequestDict](the_plaid_api/models/processor_liabilities_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorLiabilitiesGetResponse](the_plaid_api/models/processor_liabilities_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorLiabilitiesGetResponse](the_plaid_api/models/processor_liabilities_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_decision_report(body: ProcessorSignalDecisionReportRequest | ProcessorSignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorSignalDecisionReportResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

After you call `/processor/signal/evaluate`, Plaid will normally infer the outcome from your Signal Rules. However, if you are not using Signal Rules, if the Signal Rules outcome was `REVIEW`, or if you take a different action than the one determined by the Signal Rules, you will need to call `/processor/signal/decision/report`. This helps improve Signal Transaction Score accuracy for your account and is necessary for proper functioning of the rule performance and rule tuning capabilities in the Dashboard. If your effective decision changes after calling `/processor/signal/decision/report` (for example, you indicated that you accepted a transaction, but later on, your payment processor rejected it, so it was never initiated), call `/processor/signal/decision/report` again for the transaction to correct Plaid's records.

If you are using Plaid Transfer as your payment processor, you also do not need to call `/processor/signal/decision/report`, as Plaid can infer outcomes from your Transfer activity.

If using a Balance-only ruleset, this endpoint will not impact scores (Balance does not use scores), but is necessary to view accurate transaction outcomes and tune rule logic in the Dashboard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_signal_decision_report(
    ProcessorSignalDecisionReportRequest(
        processor_token="some example string", client_transaction_id="some example string", initiated=True
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalDecisionReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_signal_decision_report(
    ProcessorSignalDecisionReportRequest(
        processor_token="some example string", client_transaction_id="some example string", initiated=True
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalDecisionReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorSignalDecisionReportRequest](the_plaid_api/models/processor_signal_decision_report_request.py) \| [ProcessorSignalDecisionReportRequestDict](the_plaid_api/models/processor_signal_decision_report_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorSignalDecisionReportResponse](the_plaid_api/models/processor_signal_decision_report_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorSignalDecisionReportResponse](the_plaid_api/models/processor_signal_decision_report_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_evaluate(body: ProcessorSignalEvaluateRequest | ProcessorSignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorSignalEvaluateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/processor/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment and additional risk signals.

`/processor/signal/evaluate` uses Rulesets that are configured on the end customer's Dashboard and can be used with either the Signal Transaction Scores product or the Balance product. Which product is used will be determined by the `ruleset_key` that you provide. Note that only customer-configured rulesets work with this endpoint; as a processor partner, you cannot create or configure your own rulesets. For more details, see [Signal Rules](https://plaid.com/docs/signal/signal-rules/).

Note: This request may have higher latency if Signal Transaction Scores is being added to an existing Item for the first time, or when using a Balance-only ruleset. This is because Plaid must communicate directly with the institution to request data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_signal_evaluate(
    ProcessorSignalEvaluateRequest(
        processor_token="some example string", client_transaction_id="some example string", amount=1.5
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalEvaluateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_signal_evaluate(
    ProcessorSignalEvaluateRequest(
        processor_token="some example string", client_transaction_id="some example string", amount=1.5
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalEvaluateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorSignalEvaluateRequest](the_plaid_api/models/processor_signal_evaluate_request.py) \| [ProcessorSignalEvaluateRequestDict](the_plaid_api/models/processor_signal_evaluate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorSignalEvaluateResponse](the_plaid_api/models/processor_signal_evaluate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorSignalEvaluateResponse](the_plaid_api/models/processor_signal_evaluate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_prepare(body: ProcessorSignalPrepareRequest | ProcessorSignalPrepareRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorSignalPrepareResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

When a processor token is not initialized with `signal`, call `/processor/signal/prepare` to opt-in that processor token to the data collection process, which will improve the accuracy of the Signal Transaction Score.

If this endpoint is called with a processor token that is already initialized with `signal`, it will return a 200 response and will not modify the processor token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_signal_prepare(
    ProcessorSignalPrepareRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalPrepareResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_signal_prepare(
    ProcessorSignalPrepareRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalPrepareResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorSignalPrepareRequest](the_plaid_api/models/processor_signal_prepare_request.py) \| [ProcessorSignalPrepareRequestDict](the_plaid_api/models/processor_signal_prepare_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorSignalPrepareResponse](the_plaid_api/models/processor_signal_prepare_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorSignalPrepareResponse](the_plaid_api/models/processor_signal_prepare_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_return_report(body: ProcessorSignalReturnReportRequest | ProcessorSignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorSignalReturnReportResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Call the `/processor/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/processor/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

If you are using the [Plaid Transfer product](https://plaid.com/docs/transfer) to create transfers, it is not necessary to use this endpoint, as Plaid already knows whether the transfer was returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_signal_return_report(
    ProcessorSignalReturnReportRequest(
        processor_token="some example string",
        client_transaction_id="some example string",
        return_code="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalReturnReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_signal_return_report(
    ProcessorSignalReturnReportRequest(
        processor_token="some example string",
        client_transaction_id="some example string",
        return_code="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorSignalReturnReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorSignalReturnReportRequest](the_plaid_api/models/processor_signal_return_report_request.py) \| [ProcessorSignalReturnReportRequestDict](the_plaid_api/models/processor_signal_return_report_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorSignalReturnReportResponse](the_plaid_api/models/processor_signal_return_report_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorSignalReturnReportResponse](the_plaid_api/models/processor_signal_return_report_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_stripe_bank_account_token_create(body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorStripeBankAccountTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).

Note that the Stripe bank account token is a one-time use token. To store bank account information for later use, you can use a Stripe customer object and create an associated bank account from the token, or you can use a Stripe Custom account and create an associated external bank account from the token. This bank account information should work indefinitely, unless the user's bank account information changes or they revoke Plaid's permissions to access their account. Stripe bank account information cannot be modified once the bank account token has been created. If you ever need to change the bank account details used by Stripe for a specific customer, have the user go through Link again and create a new bank account token from the new `access_token`.

To revoke a bank account token, the entire underlying access token must be revoked using `/item/remove`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_stripe_bank_account_token_create(
    ProcessorStripeBankAccountTokenCreateRequest(access_token="some example string", account_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorStripeBankAccountTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_stripe_bank_account_token_create(
    ProcessorStripeBankAccountTokenCreateRequest(access_token="some example string", account_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorStripeBankAccountTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorStripeBankAccountTokenCreateRequest](the_plaid_api/models/processor_stripe_bank_account_token_create_request.py) \| [ProcessorStripeBankAccountTokenCreateRequestDict](the_plaid_api/models/processor_stripe_bank_account_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorStripeBankAccountTokenCreateResponse](the_plaid_api/models/processor_stripe_bank_account_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorStripeBankAccountTokenCreateResponse](the_plaid_api/models/processor_stripe_bank_account_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_create(body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. If using multiple processors, multiple different processor tokens can be created for a single access token. Once created, a processor token for a given Item can be modified by calling `/processor/token/permissions/set`. To revoke the processor's access, the entire Item must be deleted by calling `/item/remove`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_token_create(
    ProcessorTokenCreateRequest(
        access_token="some example string", account_id="some example string", processor=Processor.DWOLLA
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_token_create(
    ProcessorTokenCreateRequest(
        access_token="some example string", account_id="some example string", processor=Processor.DWOLLA
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTokenCreateRequest](the_plaid_api/models/processor_token_create_request.py) \| [ProcessorTokenCreateRequestDict](the_plaid_api/models/processor_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_permissions_get(body: ProcessorTokenPermissionsGetRequest | ProcessorTokenPermissionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTokenPermissionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to get a processor token's product permissions. The `products` field will be an empty list if the processor can access all available products.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_token_permissions_get(
    ProcessorTokenPermissionsGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenPermissionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_token_permissions_get(
    ProcessorTokenPermissionsGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenPermissionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTokenPermissionsGetRequest](the_plaid_api/models/processor_token_permissions_get_request.py) \| [ProcessorTokenPermissionsGetRequestDict](the_plaid_api/models/processor_token_permissions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTokenPermissionsGetResponse](the_plaid_api/models/processor_token_permissions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTokenPermissionsGetResponse](the_plaid_api/models/processor_token_permissions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_permissions_set(body: ProcessorTokenPermissionsSetRequest | ProcessorTokenPermissionsSetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTokenPermissionsSetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to control a processor's access to products on the given processor token. By default, a processor will have access to all available products on the corresponding item. To restrict access to a particular set of products, call this endpoint with the desired products. To restore access to all available products, call this endpoint with an empty list. This endpoint can be called multiple times as your needs and your processor's needs change.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_token_permissions_set(
    ProcessorTokenPermissionsSetRequest(processor_token="some example string", products=[Products.ASSETS])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenPermissionsSetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_token_permissions_set(
    ProcessorTokenPermissionsSetRequest(processor_token="some example string", products=[Products.ASSETS])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenPermissionsSetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTokenPermissionsSetRequest](the_plaid_api/models/processor_token_permissions_set_request.py) \| [ProcessorTokenPermissionsSetRequestDict](the_plaid_api/models/processor_token_permissions_set_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTokenPermissionsSetResponse](the_plaid_api/models/processor_token_permissions_set_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTokenPermissionsSetResponse](the_plaid_api/models/processor_token_permissions_set_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_webhook_update(body: ProcessorTokenWebhookUpdateRequest | ProcessorTokenWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTokenWebhookUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows you, the processor, to update the webhook URL associated with a processor token. This request triggers a `WEBHOOK_UPDATE_ACKNOWLEDGED` webhook to the newly specified webhook URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_token_webhook_update(
    ProcessorTokenWebhookUpdateRequest(processor_token="some example string", webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenWebhookUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_token_webhook_update(
    ProcessorTokenWebhookUpdateRequest(processor_token="some example string", webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTokenWebhookUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTokenWebhookUpdateRequest](the_plaid_api/models/processor_token_webhook_update_request.py) \| [ProcessorTokenWebhookUpdateRequestDict](the_plaid_api/models/processor_token_webhook_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTokenWebhookUpdateResponse](the_plaid_api/models/processor_token_webhook_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTokenWebhookUpdateResponse](the_plaid_api/models/processor_token_webhook_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_get(body: ProcessorTransactionsGetRequest | ProcessorTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTransactionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student` or `mortgage`; coverage may be limited). Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/processor/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).

Due to the potentially large number of transactions associated with a processor token, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.

Data returned by `/processor/transactions/get` will be the data available for the processor token as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. To force Plaid to check for new transactions, you can use the `/processor/transactions/refresh` endpoint.

Note that data may not be immediately available to `/processor/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/processor/transactions/get`, if it wasn't. If no transaction history is ready when `/processor/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

To receive Transactions webhooks for a processor token, set its webhook URL via the https://plaid.com/docs/api/processor-partners/#processortokenwebhookupdate endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_transactions_get(
    ProcessorTransactionsGetRequest(
        processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_transactions_get(
    ProcessorTransactionsGetRequest(
        processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTransactionsGetRequest](the_plaid_api/models/processor_transactions_get_request.py) \| [ProcessorTransactionsGetRequestDict](the_plaid_api/models/processor_transactions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTransactionsGetResponse](the_plaid_api/models/processor_transactions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTransactionsGetResponse](the_plaid_api/models/processor_transactions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_recurring_get(body: ProcessorTransactionsRecurringGetRequest | ProcessorTransactionsRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTransactionsRecurringGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user's checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.

This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

This endpoint can only be called on a processor token that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/processor/transactions/get` or `/processor/transactions/sync`). Once all historical transactions have been fetched, call `/processor/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the https://plaid.com/docs/api/products/transactions/#recurring_transactions_update webhook. To know when historical transactions have been fetched, if you are using `/processor/transactions/sync` listen for the https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/processor/transactions/get`, listen for the https://plaid.com/docs/api/products/transactions/#historical_update webhook.

After the initial call, you can call the `/processor/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the https://plaid.com/docs/api/products/transactions/#recurring_transactions_update webhook to be notified when new updates are available.

To receive Transactions webhooks for a processor token, set its webhook URL via the https://plaid.com/docs/api/processor-partners/#processortokenwebhookupdate endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_transactions_recurring_get(
    ProcessorTransactionsRecurringGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsRecurringGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_transactions_recurring_get(
    ProcessorTransactionsRecurringGetRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsRecurringGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTransactionsRecurringGetRequest](the_plaid_api/models/processor_transactions_recurring_get_request.py) \| [ProcessorTransactionsRecurringGetRequestDict](the_plaid_api/models/processor_transactions_recurring_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTransactionsRecurringGetResponse](the_plaid_api/models/processor_transactions_recurring_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTransactionsRecurringGetResponse](the_plaid_api/models/processor_transactions_recurring_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_refresh(body: ProcessorTransactionsRefreshRequest | ProcessorTransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTransactionsRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/processor/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for a processor token. This on-demand extraction takes place in addition to the periodic extractions that automatically occur one or more times per day for any Transactions-enabled processor token. If changes to transactions are discovered after calling `/processor/transactions/refresh`, Plaid will fire a webhook: for `/processor/transactions/sync` users, https://plaid.com/docs/api/products/transactions/#sync_updates_available will be fired if there are any transactions updated, added, or removed. For users of both `/processor/transactions/sync` and `/processor/transactions/get`, https://plaid.com/docs/api/products/transactions/#transactions_removed will be fired if any removed transactions are detected, and https://plaid.com/docs/api/products/transactions/#default_update will be fired if any new transactions are detected. New transactions can be fetched by calling `/processor/transactions/get` or `/processor/transactions/sync`. Note that the `/processor/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) non-depository accounts and will result in a `PRODUCTS_NOT_SUPPORTED` error if called on an Item that contains only non-depository accounts from that institution.

As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints (typically less than 10 seconds, but occasionally up to 30 seconds or more); if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

`/processor/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](https://plaid.com/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_transactions_refresh(
    ProcessorTransactionsRefreshRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_transactions_refresh(
    ProcessorTransactionsRefreshRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTransactionsRefreshRequest](the_plaid_api/models/processor_transactions_refresh_request.py) \| [ProcessorTransactionsRefreshRequestDict](the_plaid_api/models/processor_transactions_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTransactionsRefreshResponse](the_plaid_api/models/processor_transactions_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTransactionsRefreshResponse](the_plaid_api/models/processor_transactions_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_sync(body: ProcessorTransactionsSyncRequest | ProcessorTransactionsSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProcessorTransactionsSyncResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/transactions/sync` endpoint retrieves transactions associated with an Item and can fetch updates using a cursor to track which updates have already been seen.

For important instructions on integrating with `/processor/transactions/sync`, see the [Transactions integration overview](https://plaid.com/docs/transactions/#integration-overview). If you are migrating from an existing integration using `/processor/transactions/get`, see the [Transactions Sync migration guide](https://plaid.com/docs/transactions/sync-migration/).

This endpoint supports `credit`, `depository`, and some `loan`-type accounts (only those with account subtype `student` or `mortgage`). For `investments` accounts, use `/investments/transactions/get` instead.

When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/processor/transactions/sync` fails when retrieving a paginated update (e.g. due to the https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination error), the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.

If transactions data is not yet available for the Item, which can happen if the Item was not initialized with transactions during the `/link/token/create` call or if `/processor/transactions/sync` was called within a few seconds of Item creation, `/processor/transactions/sync` will return empty transactions arrays.

Plaid typically checks for new transactions data between one and four times per day, depending on the institution. To find out when transactions were last updated for an Item, use the [Item Debugger](https://plaid.com/docs/account/activity/#troubleshooting-with-item-debugger) or call `/item/get`; the `item.status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/processor/transactions/refresh` endpoint.

To be alerted when new transactions are available, listen for the https://plaid.com/docs/api/products/transactions/#sync_updates_available webhook.

To receive Transactions webhooks for a processor token, set its webhook URL via the https://plaid.com/docs/api/processor-partners/#processortokenwebhookupdate endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.processor_transactions_sync(
    ProcessorTransactionsSyncRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.processor_transactions_sync(
    ProcessorTransactionsSyncRequest(processor_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProcessorTransactionsSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTransactionsSyncRequest](the_plaid_api/models/processor_transactions_sync_request.py) \| [ProcessorTransactionsSyncRequestDict](the_plaid_api/models/processor_transactions_sync_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProcessorTransactionsSyncResponse](the_plaid_api/models/processor_transactions_sync_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProcessorTransactionsSyncResponse](the_plaid_api/models/processor_transactions_sync_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def profile_network_status_get(body: ProfileNetworkStatusGetRequest | ProfileNetworkStatusGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProfileNetworkStatusGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/profile/network_status/get` endpoint can be used to check whether Plaid has a matching profile for the user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.profile_network_status_get(
    ProfileNetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProfileNetworkStatusGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.profile_network_status_get(
    ProfileNetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProfileNetworkStatusGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileNetworkStatusGetRequest](the_plaid_api/models/profile_network_status_get_request.py) \| [ProfileNetworkStatusGetRequestDict](the_plaid_api/models/profile_network_status_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProfileNetworkStatusGetResponse](the_plaid_api/models/profile_network_status_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProfileNetworkStatusGetResponse](the_plaid_api/models/profile_network_status_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_compute(body: ProtectComputeRequest | ProtectComputeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProtectComputeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Compute a Protect Trust Index score for a user. The model selected determines what is scored and what additional fields the response contains. For example, `ti-link-session-2.0` scores a completed Link session for fraud risk; `cash-advance-onboarding-1.0` scores repayment risk for a first-time cash advance and additionally populates per-amount-bucket subscores. Cash-advance models require that the user have a Plaid Item with Transactions enabled, or an Assets Report, before scoring.

The endpoint returns HTTP 400 with `error_type` = `INVALID_REQUEST` and `error_code` = `FAILED_PRECONDITION` when a required precondition is not met: for link-session models, when the Link session has not completed; for cash-advance models, when the user has not successfully linked any Item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.protect_compute(
    ProtectComputeRequest(model="some example string", user=ProtectUser())
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectComputeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.protect_compute(
    ProtectComputeRequest(model="some example string", user=ProtectUser())
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectComputeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProtectComputeRequest](the_plaid_api/models/protect_compute_request.py) \| [ProtectComputeRequestDict](the_plaid_api/models/protect_compute_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProtectComputeResponse](the_plaid_api/models/protect_compute_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProtectComputeResponse](the_plaid_api/models/protect_compute_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_event_get(body: ProtectEventGetRequest | ProtectEventGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProtectEventGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get information about a user event including Trust Index score and fraud attributes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.protect_event_get(ProtectEventGetRequest(event_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectEventGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.protect_event_get(ProtectEventGetRequest(event_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectEventGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProtectEventGetRequest](the_plaid_api/models/protect_event_get_request.py) \| [ProtectEventGetRequestDict](the_plaid_api/models/protect_event_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProtectEventGetResponse](the_plaid_api/models/protect_event_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProtectEventGetResponse](the_plaid_api/models/protect_event_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_event_send(body: ProtectEventSendRequest | ProtectEventSendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProtectEventSendResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a new event to enrich user data and optionally get a Trust Index score for the event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.protect_event_send(
    ProtectEventSendRequest(event=ProtectEvent(timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectEventSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.protect_event_send(
    ProtectEventSendRequest(event=ProtectEvent(timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectEventSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProtectEventSendRequest](the_plaid_api/models/protect_event_send_request.py) \| [ProtectEventSendRequestDict](the_plaid_api/models/protect_event_send_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProtectEventSendResponse](the_plaid_api/models/protect_event_send_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProtectEventSendResponse](the_plaid_api/models/protect_event_send_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_report_create(body: ProtectReportCreateRequest | ProtectReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProtectReportCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this endpoint to create a Protect report to document fraud incidents, investigation outcomes, or other risk events.
This endpoint allows you to report various types of incidents including account takeovers, identity fraud, unauthorized transactions, and other security events.
The reported data helps improve fraud detection models and provides valuable feedback to enhance the overall security of the Plaid network.
Reports can be created for confirmed incidents that have been fully investigated, or for suspected incidents that require further review.
You can associate reports with specific users, sessions, or transactions to provide comprehensive context about the incident.
Each report must include `user_id`, or an `incident_event` with at least one supported identifier: `link_session_id`, `idv_session_id`, `protect_event_id`, `signal_client_transaction_id`, or `access_token`. Context fields such as `internal_reference`, `time`, `amount`, and `bank_account` do not satisfy this identifier requirement.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.protect_report_create(
    ProtectReportCreateRequest(
        report_confidence=ProtectReportConfidence.CONFIRMED,
        report_type=ProtectReportType.USER_ACCOUNT_TAKEOVER,
        report_source=ProtectReportSource.INTERNAL_REVIEW,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.protect_report_create(
    ProtectReportCreateRequest(
        report_confidence=ProtectReportConfidence.CONFIRMED,
        report_type=ProtectReportType.USER_ACCOUNT_TAKEOVER,
        report_source=ProtectReportSource.INTERNAL_REVIEW,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProtectReportCreateRequest](the_plaid_api/models/protect_report_create_request.py) \| [ProtectReportCreateRequestDict](the_plaid_api/models/protect_report_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProtectReportCreateResponse](the_plaid_api/models/protect_report_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProtectReportCreateResponse](the_plaid_api/models/protect_report_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_user_insights_get(body: ProtectUserInsightsGetRequest | ProtectUserInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProtectUserInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this endpoint to get basic information about a user as it relates to their fraud profile with Protect.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.protect_user_insights_get(ProtectUserInsightsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectUserInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.protect_user_insights_get(ProtectUserInsightsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProtectUserInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProtectUserInsightsGetRequest](the_plaid_api/models/protect_user_insights_get_request.py) \| [ProtectUserInsightsGetRequestDict](the_plaid_api/models/protect_user_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[ProtectUserInsightsGetResponse](the_plaid_api/models/protect_user_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProtectUserInsightsGetResponse](the_plaid_api/models/protect_user_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_bank_income_fire_webhook(body: SandboxBankIncomeFireWebhookRequest | SandboxBankIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxBankIncomeFireWebhookResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/bank_income/fire_webhook` endpoint to manually trigger a Bank Income webhook in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_bank_income_fire_webhook(
    SandboxBankIncomeFireWebhookRequest(
        webhook_code=SandboxBankIncomeWebhookFireRequestWebhookCode.BANK_INCOME_REFRESH_UPDATE,
        webhook_fields=SandboxBankIncomeWebhookFireRequestWebhookFields(user_id="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxBankIncomeFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_bank_income_fire_webhook(
    SandboxBankIncomeFireWebhookRequest(
        webhook_code=SandboxBankIncomeWebhookFireRequestWebhookCode.BANK_INCOME_REFRESH_UPDATE,
        webhook_fields=SandboxBankIncomeWebhookFireRequestWebhookFields(user_id="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxBankIncomeFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxBankIncomeFireWebhookRequest](the_plaid_api/models/sandbox_bank_income_fire_webhook_request.py) \| [SandboxBankIncomeFireWebhookRequestDict](the_plaid_api/models/sandbox_bank_income_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxBankIncomeFireWebhookResponse](the_plaid_api/models/sandbox_bank_income_fire_webhook_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxBankIncomeFireWebhookResponse](the_plaid_api/models/sandbox_bank_income_fire_webhook_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_bank_transfer_fire_webhook(body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxBankTransferFireWebhookResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_bank_transfer_fire_webhook(
    SandboxBankTransferFireWebhookRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxBankTransferFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_bank_transfer_fire_webhook(
    SandboxBankTransferFireWebhookRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxBankTransferFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxBankTransferFireWebhookRequest](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py) \| [SandboxBankTransferFireWebhookRequestDict](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxBankTransferFireWebhookResponse](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxBankTransferFireWebhookResponse](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_bank_transfer_simulate(body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxBankTransferSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_bank_transfer_simulate(
    SandboxBankTransferSimulateRequest(bank_transfer_id="some example string", event_type="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxBankTransferSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_bank_transfer_simulate(
    SandboxBankTransferSimulateRequest(bank_transfer_id="some example string", event_type="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxBankTransferSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxBankTransferSimulateRequest](the_plaid_api/models/sandbox_bank_transfer_simulate_request.py) \| [SandboxBankTransferSimulateRequestDict](the_plaid_api/models/sandbox_bank_transfer_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxBankTransferSimulateResponse](the_plaid_api/models/sandbox_bank_transfer_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxBankTransferSimulateResponse](the_plaid_api/models/sandbox_bank_transfer_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_cra_cashflow_updates_update(body: SandboxCraCashflowUpdatesUpdateRequest | SandboxCraCashflowUpdatesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxCraCashflowUpdatesUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/cra/cashflow_updates/update` endpoint to manually trigger an update for Cash Flow Updates (Monitoring) in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_cra_cashflow_updates_update(SandboxCraCashflowUpdatesUpdateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxCraCashflowUpdatesUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_cra_cashflow_updates_update(
    SandboxCraCashflowUpdatesUpdateRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxCraCashflowUpdatesUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxCraCashflowUpdatesUpdateRequest](the_plaid_api/models/sandbox_cra_cashflow_updates_update_request.py) \| [SandboxCraCashflowUpdatesUpdateRequestDict](the_plaid_api/models/sandbox_cra_cashflow_updates_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxCraCashflowUpdatesUpdateResponse](the_plaid_api/models/sandbox_cra_cashflow_updates_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxCraCashflowUpdatesUpdateResponse](the_plaid_api/models/sandbox_cra_cashflow_updates_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_fdx_consent_seed(body: SandboxFdxConsentSeedRequest | SandboxFdxConsentSeedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxFdxConsentSeedResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/sandbox/fdx/consent/seed` creates a test FDX consent grant (and a backing Item) for a data provider's customer in Sandbox, so the FDX Consent API endpoints can be exercised end-to-end without a live data provider connection.

`customer_id` is the data provider's identifier for the end user and `application_id` identifies the data recipient application the consent is granted to; both are required. Optionally provide `consent_id` (a UUIDv4) to control the seeded grant's identifier; one is generated when omitted. The seeded grant is returned by `/fdx/consents` and `/fdx/consents/{consentId}`, and can be revoked via `/fdx/consents/{consentId}/revocation`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_fdx_consent_seed(
    SandboxFdxConsentSeedRequest(customer_id="some example string", application_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxFdxConsentSeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_fdx_consent_seed(
    SandboxFdxConsentSeedRequest(customer_id="some example string", application_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxFdxConsentSeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxFdxConsentSeedRequest](the_plaid_api/models/sandbox_fdx_consent_seed_request.py) \| [SandboxFdxConsentSeedRequestDict](the_plaid_api/models/sandbox_fdx_consent_seed_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxFdxConsentSeedResponse](the_plaid_api/models/sandbox_fdx_consent_seed_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxFdxConsentSeedResponse](the_plaid_api/models/sandbox_fdx_consent_seed_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_income_fire_webhook(body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxIncomeFireWebhookResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/income/fire_webhook` endpoint to manually trigger a Payroll or Document Income webhook in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_income_fire_webhook(
    SandboxIncomeFireWebhookRequest(
        item_id="some example string",
        webhook="some example string",
        webhook_code=SandboxIncomeWebhookFireRequestWebhookCode.INCOME_VERIFICATION,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxIncomeFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_income_fire_webhook(
    SandboxIncomeFireWebhookRequest(
        item_id="some example string",
        webhook="some example string",
        webhook_code=SandboxIncomeWebhookFireRequestWebhookCode.INCOME_VERIFICATION,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxIncomeFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxIncomeFireWebhookRequest](the_plaid_api/models/sandbox_income_fire_webhook_request.py) \| [SandboxIncomeFireWebhookRequestDict](the_plaid_api/models/sandbox_income_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxIncomeFireWebhookResponse](the_plaid_api/models/sandbox_income_fire_webhook_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxIncomeFireWebhookResponse](the_plaid_api/models/sandbox_income_fire_webhook_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_application_seed(body: SandboxItemApplicationSeedRequest | SandboxItemApplicationSeedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxItemApplicationSeedResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/sandbox/item/application/seed` creates a test connected application on an existing Permissions Manager Item's login. The seeded application will appear in subsequent calls to `/item/application/list`.

The `access_token` must belong to a Permissions Manager Item created via `/item/import` in Sandbox. The `application_id` identifies the application to seed as a connected app. To disconnect a seeded application, use `/item/application/unlink`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_item_application_seed(
    SandboxItemApplicationSeedRequest(access_token="some example string", application_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemApplicationSeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_item_application_seed(
    SandboxItemApplicationSeedRequest(access_token="some example string", application_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemApplicationSeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxItemApplicationSeedRequest](the_plaid_api/models/sandbox_item_application_seed_request.py) \| [SandboxItemApplicationSeedRequestDict](the_plaid_api/models/sandbox_item_application_seed_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxItemApplicationSeedResponse](the_plaid_api/models/sandbox_item_application_seed_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxItemApplicationSeedResponse](the_plaid_api/models/sandbox_item_application_seed_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_fire_webhook(body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxItemFireWebhookResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:

`DEFAULT_UPDATE`: Webhook to be fired for a given Sandbox Item simulating a default update event for the respective product as specified with the `webhook_type` in the request body. Valid Sandbox `DEFAULT_UPDATE` webhook types include: `AUTH`, `IDENTITY`, `TRANSACTIONS`, `INVESTMENTS_TRANSACTIONS`, `LIABILITIES`, `HOLDINGS`. If the Item does not support the product, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`NEW_ACCOUNTS_AVAILABLE`: Fired to indicate that a new account is available on the Item and you can launch update mode to request access to it.

`SMS_MICRODEPOSITS_VERIFICATION`: Fired when a given Same-Day Micro-deposit Item is verified via SMS verification.

`LOGIN_REPAIRED`: Fired when an Item recovers from the `ITEM_LOGIN_REQUIRED` without the user going through update mode in your app.

`PENDING_DISCONNECT`: Fired when an Item will stop working in the near future (e.g. due to a planned bank migration) and must be sent through update mode to continue working.

`RECURRING_TRANSACTIONS_UPDATE`: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`SYNC_UPDATES_AVAILABLE`: Transactions webhook to be fired for a given Sandbox Item.  If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`PRODUCT_READY`: Assets webhook to be fired when a given asset report has been successfully generated. If the Item does not support Assets, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`ERROR`: Assets webhook to be fired when asset report generation has failed. If the Item does not support Assets, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`USER_PERMISSION_REVOKED`: Indicates an end user has revoked the permission that they previously granted to access an Item. May not always fire upon revocation, as some institutions' consent portals do not trigger this webhook. Upon receiving this webhook, it is recommended to delete any stored data from Plaid associated with the account or Item.

`USER_ACCOUNT_REVOKED`: Fired when an end user has revoked access to their account on the Data Provider's portal. This webhook is currently sent only for PNC Items, but may be sent in the future for other financial institutions. Upon receiving this webhook, it is recommended to delete any stored data from Plaid associated with the account or Item.

Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production (except for webhooks of type `TRANSFER`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_item_fire_webhook(
    SandboxItemFireWebhookRequest(access_token="some example string", webhook_code=WebhookCode.DEFAULT_UPDATE)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_item_fire_webhook(
    SandboxItemFireWebhookRequest(access_token="some example string", webhook_code=WebhookCode.DEFAULT_UPDATE)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxItemFireWebhookRequest](the_plaid_api/models/sandbox_item_fire_webhook_request.py) \| [SandboxItemFireWebhookRequestDict](the_plaid_api/models/sandbox_item_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxItemFireWebhookResponse](the_plaid_api/models/sandbox_item_fire_webhook_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxItemFireWebhookResponse](the_plaid_api/models/sandbox_item_fire_webhook_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_reset_login(body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxItemResetLoginResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/sandbox/item/reset_login` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, you can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.
In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_item_reset_login(
    SandboxItemResetLoginRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemResetLoginResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_item_reset_login(
    SandboxItemResetLoginRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemResetLoginResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxItemResetLoginRequest](the_plaid_api/models/sandbox_item_reset_login_request.py) \| [SandboxItemResetLoginRequestDict](the_plaid_api/models/sandbox_item_reset_login_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxItemResetLoginResponse](the_plaid_api/models/sandbox_item_reset_login_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxItemResetLoginResponse](the_plaid_api/models/sandbox_item_reset_login_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_set_verification_status(body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxItemSetVerificationStatusResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in the Sandbox in order to simulate the Automated Micro-deposit flow.

For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_item_set_verification_status(
    SandboxItemSetVerificationStatusRequest(
        access_token="some example string",
        account_id="some example string",
        verification_status=VerificationStatus1.AUTOMATICALLY_VERIFIED,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemSetVerificationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_item_set_verification_status(
    SandboxItemSetVerificationStatusRequest(
        access_token="some example string",
        account_id="some example string",
        verification_status=VerificationStatus1.AUTOMATICALLY_VERIFIED,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxItemSetVerificationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxItemSetVerificationStatusRequest](the_plaid_api/models/sandbox_item_set_verification_status_request.py) \| [SandboxItemSetVerificationStatusRequestDict](the_plaid_api/models/sandbox_item_set_verification_status_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxItemSetVerificationStatusResponse](the_plaid_api/models/sandbox_item_set_verification_status_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxItemSetVerificationStatusResponse](the_plaid_api/models/sandbox_item_set_verification_status_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_oauth_select_accounts(body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save the selected accounts when connecting to the Platypus OAuth institution

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_oauth_select_accounts(
    SandboxOauthSelectAccountsRequest(oauth_state_id="some example string", accounts=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_oauth_select_accounts(
    SandboxOauthSelectAccountsRequest(oauth_state_id="some example string", accounts=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxOauthSelectAccountsRequest](the_plaid_api/models/sandbox_oauth_select_accounts_request.py) \| [SandboxOauthSelectAccountsRequestDict](the_plaid_api/models/sandbox_oauth_select_accounts_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;Any, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_payment_profile_reset_login(body: SandboxPaymentProfileResetLoginRequest | SandboxPaymentProfileResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxPaymentProfileResetLoginResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/sandbox/payment_profile/reset_login` forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.

After calling `/sandbox/payment_profile/reset_login`, calls to the `/transfer/authorization/create` with the Payment Profile will result in a `decision_rationale` `PAYMENT_PROFILE_LOGIN_REQUIRED`. You can then use update mode for Payment Profile to restore it into a good state.

 In order to invoke this endpoint, you must first [create a Payment Profile](https://plaid.com/docs/transfer/add-to-app/#create-a-payment-profile-optional) and [go through the Link flow](https://plaid.com/docs/transfer/add-to-app/#create-a-link-token).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_payment_profile_reset_login(
    SandboxPaymentProfileResetLoginRequest(payment_profile_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxPaymentProfileResetLoginResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_payment_profile_reset_login(
    SandboxPaymentProfileResetLoginRequest(payment_profile_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxPaymentProfileResetLoginResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxPaymentProfileResetLoginRequest](the_plaid_api/models/sandbox_payment_profile_reset_login_request.py) \| [SandboxPaymentProfileResetLoginRequestDict](the_plaid_api/models/sandbox_payment_profile_reset_login_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxPaymentProfileResetLoginResponse](the_plaid_api/models/sandbox_payment_profile_reset_login_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxPaymentProfileResetLoginResponse](the_plaid_api/models/sandbox_payment_profile_reset_login_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_payment_simulate(body: SandboxPaymentSimulateRequest | SandboxPaymentSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxPaymentSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/payment/simulate` endpoint to simulate various payment events in the Sandbox environment. This endpoint will trigger the corresponding payment status webhook.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_payment_simulate(
    SandboxPaymentSimulateRequest(
        payment_id="some example string", webhook="some example string", status="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxPaymentSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_payment_simulate(
    SandboxPaymentSimulateRequest(
        payment_id="some example string", webhook="some example string", status="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxPaymentSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxPaymentSimulateRequest](the_plaid_api/models/sandbox_payment_simulate_request.py) \| [SandboxPaymentSimulateRequestDict](the_plaid_api/models/sandbox_payment_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxPaymentSimulateResponse](the_plaid_api/models/sandbox_payment_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxPaymentSimulateResponse](the_plaid_api/models/sandbox_payment_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_processor_token_create(body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxProcessorTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_processor_token_create(
    SandboxProcessorTokenCreateRequest(institution_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxProcessorTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_processor_token_create(
    SandboxProcessorTokenCreateRequest(institution_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxProcessorTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxProcessorTokenCreateRequest](the_plaid_api/models/sandbox_processor_token_create_request.py) \| [SandboxProcessorTokenCreateRequestDict](the_plaid_api/models/sandbox_processor_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxProcessorTokenCreateResponse](the_plaid_api/models/sandbox_processor_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxProcessorTokenCreateResponse](the_plaid_api/models/sandbox_processor_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_public_token_create(body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxPublicTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/public_token/create` endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data, or with Plaid's [pre-populated Sandbox test accounts](https://plaid.com/docs/sandbox/test-credentials/).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_public_token_create(
    SandboxPublicTokenCreateRequest(institution_id="some example string", initial_products=[Products.ASSETS])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxPublicTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_public_token_create(
    SandboxPublicTokenCreateRequest(institution_id="some example string", initial_products=[Products.ASSETS])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxPublicTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxPublicTokenCreateRequest](the_plaid_api/models/sandbox_public_token_create_request.py) \| [SandboxPublicTokenCreateRequestDict](the_plaid_api/models/sandbox_public_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxPublicTokenCreateResponse](the_plaid_api/models/sandbox_public_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxPublicTokenCreateResponse](the_plaid_api/models/sandbox_public_token_create_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transactions_create(body: SandboxTransactionsCreateRequest | SandboxTransactionsCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransactionsCreateResponse, SandboxTransactionsCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transactions/create` endpoint to create new transactions for an existing Item. This endpoint can be used to add up to 10 transactions to any Item at a time.

This endpoint can only be used with Items that were created in the Sandbox environment using the `user_transactions_dynamic` test user. You can use this to add transactions to test the `/transactions/get` and `/transactions/sync` endpoints.

Custom transactions are only applied to the depository account. Support for per-account targeting may be added in the future.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transactions_create(
    SandboxTransactionsCreateRequest(
        access_token="some example string",
        transactions=[
            CustomSandboxTransaction(
                date_transacted=date(2024, 1, 15),
                date_posted=date(2024, 1, 15),
                amount=1.5,
                description="some example string",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransactionsCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SandboxTransactionsCreateErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transactions_create(
    SandboxTransactionsCreateRequest(
        access_token="some example string",
        transactions=[
            CustomSandboxTransaction(
                date_transacted=date(2024, 1, 15),
                date_posted=date(2024, 1, 15),
                amount=1.5,
                description="some example string",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransactionsCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SandboxTransactionsCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransactionsCreateRequest](the_plaid_api/models/sandbox_transactions_create_request.py) \| [SandboxTransactionsCreateRequestDict](the_plaid_api/models/sandbox_transactions_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransactionsCreateResponse](the_plaid_api/models/sandbox_transactions_create_response.py), [SandboxTransactionsCreateErrorBody](the_plaid_api/errors/sandbox_transactions_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransactionsCreateResponse](the_plaid_api/models/sandbox_transactions_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[SandboxTransactionsCreateErrorBody](the_plaid_api/errors/sandbox_transactions_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](the_plaid_api/models/error.py) \| None</code> |
| anything unmapped | <code>[RawError](the_plaid_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_fire_webhook(body: SandboxTransferFireWebhookRequest | SandboxTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferFireWebhookResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/fire_webhook` endpoint to manually trigger a `TRANSFER_EVENTS_UPDATE` webhook in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_fire_webhook(
    SandboxTransferFireWebhookRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_fire_webhook(
    SandboxTransferFireWebhookRequest(webhook="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferFireWebhookResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferFireWebhookRequest](the_plaid_api/models/sandbox_transfer_fire_webhook_request.py) \| [SandboxTransferFireWebhookRequestDict](the_plaid_api/models/sandbox_transfer_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferFireWebhookResponse](the_plaid_api/models/sandbox_transfer_fire_webhook_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferFireWebhookResponse](the_plaid_api/models/sandbox_transfer_fire_webhook_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_ledger_deposit_simulate(body: SandboxTransferLedgerDepositSimulateRequest | SandboxTransferLedgerDepositSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferLedgerDepositSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/ledger/deposit/simulate` endpoint to simulate a ledger deposit event in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_ledger_deposit_simulate(
    SandboxTransferLedgerDepositSimulateRequest(
        sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferLedgerDepositSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_ledger_deposit_simulate(
    SandboxTransferLedgerDepositSimulateRequest(
        sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferLedgerDepositSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferLedgerDepositSimulateRequest](the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_request.py) \| [SandboxTransferLedgerDepositSimulateRequestDict](the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferLedgerDepositSimulateResponse](the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferLedgerDepositSimulateResponse](the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_ledger_simulate_available(body: SandboxTransferLedgerSimulateAvailableRequest | SandboxTransferLedgerSimulateAvailableRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferLedgerSimulateAvailableResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/ledger/simulate_available` endpoint to simulate converting pending balance to available balance for all originators in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_ledger_simulate_available(
    SandboxTransferLedgerSimulateAvailableRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferLedgerSimulateAvailableResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_ledger_simulate_available(
    SandboxTransferLedgerSimulateAvailableRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferLedgerSimulateAvailableResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferLedgerSimulateAvailableRequest](the_plaid_api/models/sandbox_transfer_ledger_simulate_available_request.py) \| [SandboxTransferLedgerSimulateAvailableRequestDict](the_plaid_api/models/sandbox_transfer_ledger_simulate_available_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferLedgerSimulateAvailableResponse](the_plaid_api/models/sandbox_transfer_ledger_simulate_available_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferLedgerSimulateAvailableResponse](the_plaid_api/models/sandbox_transfer_ledger_simulate_available_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_ledger_withdraw_simulate(body: SandboxTransferLedgerWithdrawSimulateRequest | SandboxTransferLedgerWithdrawSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferLedgerWithdrawSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/ledger/withdraw/simulate` endpoint to simulate a ledger withdraw event in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_ledger_withdraw_simulate(
    SandboxTransferLedgerWithdrawSimulateRequest(
        sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferLedgerWithdrawSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_ledger_withdraw_simulate(
    SandboxTransferLedgerWithdrawSimulateRequest(
        sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferLedgerWithdrawSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferLedgerWithdrawSimulateRequest](the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_request.py) \| [SandboxTransferLedgerWithdrawSimulateRequestDict](the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferLedgerWithdrawSimulateResponse](the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferLedgerWithdrawSimulateResponse](the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_refund_simulate(body: SandboxTransferRefundSimulateRequest | SandboxTransferRefundSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferRefundSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/refund/simulate` endpoint to simulate a refund event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_refund_simulate(
    SandboxTransferRefundSimulateRequest(refund_id="some example string", event_type="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferRefundSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_refund_simulate(
    SandboxTransferRefundSimulateRequest(refund_id="some example string", event_type="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferRefundSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferRefundSimulateRequest](the_plaid_api/models/sandbox_transfer_refund_simulate_request.py) \| [SandboxTransferRefundSimulateRequestDict](the_plaid_api/models/sandbox_transfer_refund_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferRefundSimulateResponse](the_plaid_api/models/sandbox_transfer_refund_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferRefundSimulateResponse](the_plaid_api/models/sandbox_transfer_refund_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_repayment_simulate(body: SandboxTransferRepaymentSimulateRequest | SandboxTransferRepaymentSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferRepaymentSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/repayment/simulate` endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, a 400 error is returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_repayment_simulate(SandboxTransferRepaymentSimulateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferRepaymentSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_repayment_simulate(
    SandboxTransferRepaymentSimulateRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferRepaymentSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferRepaymentSimulateRequest](the_plaid_api/models/sandbox_transfer_repayment_simulate_request.py) \| [SandboxTransferRepaymentSimulateRequestDict](the_plaid_api/models/sandbox_transfer_repayment_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferRepaymentSimulateResponse](the_plaid_api/models/sandbox_transfer_repayment_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferRepaymentSimulateResponse](the_plaid_api/models/sandbox_transfer_repayment_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_simulate(body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_simulate(
    SandboxTransferSimulateRequest(transfer_id="some example string", event_type="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_simulate(
    SandboxTransferSimulateRequest(transfer_id="some example string", event_type="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferSimulateRequest](the_plaid_api/models/sandbox_transfer_simulate_request.py) \| [SandboxTransferSimulateRequestDict](the_plaid_api/models/sandbox_transfer_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferSimulateResponse](the_plaid_api/models/sandbox_transfer_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferSimulateResponse](the_plaid_api/models/sandbox_transfer_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_sweep_simulate(body: SandboxTransferSweepSimulateRequest | SandboxTransferSweepSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferSweepSimulateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all transfers with a sweep status of `swept` will become `swept_settled`, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_sweep_simulate(SandboxTransferSweepSimulateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferSweepSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_sweep_simulate(SandboxTransferSweepSimulateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferSweepSimulateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferSweepSimulateRequest](the_plaid_api/models/sandbox_transfer_sweep_simulate_request.py) \| [SandboxTransferSweepSimulateRequestDict](the_plaid_api/models/sandbox_transfer_sweep_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferSweepSimulateResponse](the_plaid_api/models/sandbox_transfer_sweep_simulate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferSweepSimulateResponse](the_plaid_api/models/sandbox_transfer_sweep_simulate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_advance(body: SandboxTransferTestClockAdvanceRequest | SandboxTransferTestClockAdvanceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferTestClockAdvanceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/advance` endpoint to advance a `test_clock` in the Sandbox environment.

A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. A test clock can be advanced by incrementing `virtual_time`, but may never go back to a lower `virtual_time`.

If a test clock is advanced, we will simulate the changes that ought to occur during the time that elapsed.

For example, a client creates a weekly recurring transfer with a test clock set at t. When the client advances the test clock by setting `virtual_time` = t + 15 days, 2 new originations should be created, along with the webhook events.

The advancement of the test clock from its current `virtual_time` should be limited such that there are no more than 20 originations resulting from the advance operation on each `recurring_transfer` associated with the `test_clock`.

For example, if the recurring transfer associated with this test clock originates once every 4 weeks, you can advance the `virtual_time` up to 80 weeks on each API call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_test_clock_advance(
    SandboxTransferTestClockAdvanceRequest(
        test_clock_id="some example string", new_virtual_time=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockAdvanceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_test_clock_advance(
    SandboxTransferTestClockAdvanceRequest(
        test_clock_id="some example string", new_virtual_time=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockAdvanceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferTestClockAdvanceRequest](the_plaid_api/models/sandbox_transfer_test_clock_advance_request.py) \| [SandboxTransferTestClockAdvanceRequestDict](the_plaid_api/models/sandbox_transfer_test_clock_advance_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferTestClockAdvanceResponse](the_plaid_api/models/sandbox_transfer_test_clock_advance_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferTestClockAdvanceResponse](the_plaid_api/models/sandbox_transfer_test_clock_advance_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_create(body: SandboxTransferTestClockCreateRequest | SandboxTransferTestClockCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferTestClockCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/create` endpoint to create a `test_clock` in the Sandbox environment.

A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. Test clocks are used for testing recurring transfers in Sandbox.

A test clock can be associated with up to 5 recurring transfers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_test_clock_create(SandboxTransferTestClockCreateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_test_clock_create(
    SandboxTransferTestClockCreateRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferTestClockCreateRequest](the_plaid_api/models/sandbox_transfer_test_clock_create_request.py) \| [SandboxTransferTestClockCreateRequestDict](the_plaid_api/models/sandbox_transfer_test_clock_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferTestClockCreateResponse](the_plaid_api/models/sandbox_transfer_test_clock_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferTestClockCreateResponse](the_plaid_api/models/sandbox_transfer_test_clock_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_get(body: SandboxTransferTestClockGetRequest | SandboxTransferTestClockGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferTestClockGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/get` endpoint to get a `test_clock` in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_test_clock_get(
    SandboxTransferTestClockGetRequest(test_clock_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_test_clock_get(
    SandboxTransferTestClockGetRequest(test_clock_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferTestClockGetRequest](the_plaid_api/models/sandbox_transfer_test_clock_get_request.py) \| [SandboxTransferTestClockGetRequestDict](the_plaid_api/models/sandbox_transfer_test_clock_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferTestClockGetResponse](the_plaid_api/models/sandbox_transfer_test_clock_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferTestClockGetResponse](the_plaid_api/models/sandbox_transfer_test_clock_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_list(body: SandboxTransferTestClockListRequest | SandboxTransferTestClockListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxTransferTestClockListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/test_clock/list` endpoint to see a list of all your test clocks in the Sandbox environment, by ascending `virtual_time`. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired test clocks.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_transfer_test_clock_list(SandboxTransferTestClockListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_transfer_test_clock_list(SandboxTransferTestClockListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxTransferTestClockListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferTestClockListRequest](the_plaid_api/models/sandbox_transfer_test_clock_list_request.py) \| [SandboxTransferTestClockListRequestDict](the_plaid_api/models/sandbox_transfer_test_clock_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxTransferTestClockListResponse](the_plaid_api/models/sandbox_transfer_test_clock_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxTransferTestClockListResponse](the_plaid_api/models/sandbox_transfer_test_clock_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_user_reset_login(body: SandboxUserResetLoginRequest | SandboxUserResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SandboxUserResetLoginResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/sandbox/user/reset_login` functions the same as `/sandbox/item/reset_login`, but will modify Items related to a User. This endpoint forces each Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/user/reset_login`, you can then use Plaid Link update mode to restore Items associated with the User to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.
In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.sandbox_user_reset_login(SandboxUserResetLoginRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxUserResetLoginResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.sandbox_user_reset_login(SandboxUserResetLoginRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SandboxUserResetLoginResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxUserResetLoginRequest](the_plaid_api/models/sandbox_user_reset_login_request.py) \| [SandboxUserResetLoginRequestDict](the_plaid_api/models/sandbox_user_reset_login_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SandboxUserResetLoginResponse](the_plaid_api/models/sandbox_user_reset_login_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SandboxUserResetLoginResponse](the_plaid_api/models/sandbox_user_reset_login_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def session_token_create(body: SessionTokenCreateRequest | SessionTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SessionTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/session/token/create` is used to create a Link token for Layer. The returned Link token is used as a parameter when initializing the Link SDK. For more details, see the [Link flow overview](https://plaid.com/docs/link/#link-flow-overview).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.session_token_create(SessionTokenCreateRequest(template_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SessionTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.session_token_create(
    SessionTokenCreateRequest(template_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SessionTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SessionTokenCreateRequest](the_plaid_api/models/session_token_create_request.py) \| [SessionTokenCreateRequestDict](the_plaid_api/models/session_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SessionTokenCreateResponse](the_plaid_api/models/session_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SessionTokenCreateResponse](the_plaid_api/models/session_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_decision_report(body: SignalDecisionReportRequest | SignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignalDecisionReportResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

After you call `/signal/evaluate`, Plaid will normally infer the outcome from your Signal Rules. However, if you are not using Signal Rules, if the Signal Rules outcome was `REVIEW`, or if you take a different action than the one determined by the Signal Rules, you will need to call `/signal/decision/report`. This helps improve Signal Transaction Score accuracy for your account and is necessary for proper functioning of the rule performance and rule tuning capabilities in the Dashboard. If your effective decision changes after calling `/signal/decision/report` (for example, you indicated that you accepted a transaction, but later on, your payment processor rejected it, so it was never initiated), call `/signal/decision/report` again for the transaction to correct Plaid's records.

If you are using Plaid Transfer as your payment processor, you also do not need to call `/signal/decision/report`, as Plaid can infer outcomes from your Transfer activity.

If using a Balance-only ruleset, this endpoint will not impact scores (Balance does not use scores), but is necessary to view accurate transaction outcomes and tune rule logic in the Dashboard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.signal_decision_report(
    SignalDecisionReportRequest(client_transaction_id="some example string", initiated=True)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalDecisionReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.signal_decision_report(
    SignalDecisionReportRequest(client_transaction_id="some example string", initiated=True)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalDecisionReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalDecisionReportRequest](the_plaid_api/models/signal_decision_report_request.py) \| [SignalDecisionReportRequestDict](the_plaid_api/models/signal_decision_report_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SignalDecisionReportResponse](the_plaid_api/models/signal_decision_report_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignalDecisionReportResponse](the_plaid_api/models/signal_decision_report_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_evaluate(body: SignalEvaluateRequest | SignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignalEvaluateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment and additional risk signals.

Before using `/signal/evaluate`, you must first [create a ruleset](https://plaid.com/docs/signal/signal-rules/) in the Dashboard under https://dashboard.plaid.com/signal/risk-profiles.

`/signal/evaluate` can be used with either Signal Transaction Scores or the Balance product. Which product is used will be determined by the `ruleset_key` that you provide. For more details, see [Signal Rules](https://plaid.com/docs/signal/signal-rules/).

Note: This request may have higher latency when using a Balance-only ruleset. This is because Plaid must communicate directly with the institution to request data. Balance-only rulesets may have latency of up to 30 seconds or more; if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.signal_evaluate(
    SignalEvaluateRequest(
        access_token="some example string",
        account_id="some example string",
        client_transaction_id="some example string",
        amount=1.5,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalEvaluateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.signal_evaluate(
    SignalEvaluateRequest(
        access_token="some example string",
        account_id="some example string",
        client_transaction_id="some example string",
        amount=1.5,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalEvaluateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalEvaluateRequest](the_plaid_api/models/signal_evaluate_request.py) \| [SignalEvaluateRequestDict](the_plaid_api/models/signal_evaluate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SignalEvaluateResponse](the_plaid_api/models/signal_evaluate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignalEvaluateResponse](the_plaid_api/models/signal_evaluate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_prepare(body: SignalPrepareRequest | SignalPrepareRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignalPrepareResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

When an Item is not initialized with `signal`, call `/signal/prepare` to opt-in that Item to the data collection process used to develop a Signal Transaction Score. This should be done on Items where `signal` was added in the `additional_consented_products` array but not in the `products`, `optional_products`, or `required_if_supported_products` array. If `/signal/prepare` is skipped on an Item that is not initialized with `signal`, the initial call to `/signal/evaluate` on that Item will be less accurate, because Plaid will have access to less data for computing the Signal Transaction Score.

If your integration is purely Balance-only, this endpoint will have no effect, as Balance-only rulesets do not calculate a Signal Transaction Score.

If run on an Item that is already initialized with `signal`, this endpoint will return a 200 response and will not modify the Item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.signal_prepare(SignalPrepareRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalPrepareResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.signal_prepare(SignalPrepareRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalPrepareResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalPrepareRequest](the_plaid_api/models/signal_prepare_request.py) \| [SignalPrepareRequestDict](the_plaid_api/models/signal_prepare_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SignalPrepareResponse](the_plaid_api/models/signal_prepare_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignalPrepareResponse](the_plaid_api/models/signal_prepare_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_return_report(body: SignalReturnReportRequest | SignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignalReturnReportResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trends into your scores and tune rule logic. If using a Balance-only ruleset, this endpoint will not impact scores (as Balance does not use scores), but is necessary to view accurate transaction outcomes and tune rule logic in the Dashboard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.signal_return_report(
    SignalReturnReportRequest(client_transaction_id="some example string", return_code="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalReturnReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.signal_return_report(
    SignalReturnReportRequest(client_transaction_id="some example string", return_code="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalReturnReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalReturnReportRequest](the_plaid_api/models/signal_return_report_request.py) \| [SignalReturnReportRequestDict](the_plaid_api/models/signal_return_report_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SignalReturnReportResponse](the_plaid_api/models/signal_return_report_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignalReturnReportResponse](the_plaid_api/models/signal_return_report_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_schedule(body: SignalScheduleRequest | SignalScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignalScheduleResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/signal/schedule` to schedule a planned ACH transaction.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.signal_schedule(
    SignalScheduleRequest(
        access_token="some example string",
        account_id="some example string",
        client_transaction_id="some example string",
        amount=1.5,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.signal_schedule(
    SignalScheduleRequest(
        access_token="some example string",
        account_id="some example string",
        client_transaction_id="some example string",
        amount=1.5,
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignalScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalScheduleRequest](the_plaid_api/models/signal_schedule_request.py) \| [SignalScheduleRequestDict](the_plaid_api/models/signal_schedule_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[SignalScheduleResponse](the_plaid_api/models/signal_schedule_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignalScheduleResponse](the_plaid_api/models/signal_schedule_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def statements_download(body: StatementsDownloadRequest | StatementsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/statements/download` endpoint retrieves a single statement PDF in binary format.  The response will contain a `Plaid-Content-Hash` header containing a SHA 256 checksum of the statement. This can be used to verify that the file being sent by Plaid is the same file that was downloaded to your system.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.statements_download(
    StatementsDownloadRequest(access_token="some example string", statement_id="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.statements_download(
    StatementsDownloadRequest(access_token="some example string", statement_id="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[StatementsDownloadRequest](the_plaid_api/models/statements_download_request.py) \| [StatementsDownloadRequestDict](the_plaid_api/models/statements_download_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;None, [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def statements_list(body: StatementsListRequest | StatementsListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StatementsListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/statements/list` endpoint retrieves a list of all statements associated with an Item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.statements_list(StatementsListRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StatementsListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.statements_list(StatementsListRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StatementsListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[StatementsListRequest](the_plaid_api/models/statements_list_request.py) \| [StatementsListRequestDict](the_plaid_api/models/statements_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[StatementsListResponse](the_plaid_api/models/statements_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StatementsListResponse](the_plaid_api/models/statements_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def statements_refresh(body: StatementsRefreshRequest | StatementsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StatementsRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/statements/refresh` initiates an on-demand extraction to fetch the statements for the provided dates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.statements_refresh(
    StatementsRefreshRequest(
        access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StatementsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.statements_refresh(
    StatementsRefreshRequest(
        access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StatementsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[StatementsRefreshRequest](the_plaid_api/models/statements_refresh_request.py) \| [StatementsRefreshRequestDict](the_plaid_api/models/statements_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[StatementsRefreshResponse](the_plaid_api/models/statements_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StatementsRefreshResponse](the_plaid_api/models/statements_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_enhance(body: TransactionsEnhanceGetRequest | TransactionsEnhanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsEnhanceGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/transactions/v1/enhance` endpoint enriches raw transaction data provided directly by clients.

The product is currently in beta.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_enhance(
    TransactionsEnhanceGetRequest(
        account_type="some example string",
        transactions=[
            ClientProvidedRawTransaction(
                id="some example string",
                description="some example string",
                amount=1.5,
                iso_currency_code="some example string",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsEnhanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_enhance(
    TransactionsEnhanceGetRequest(
        account_type="some example string",
        transactions=[
            ClientProvidedRawTransaction(
                id="some example string",
                description="some example string",
                amount=1.5,
                iso_currency_code="some example string",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsEnhanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsEnhanceGetRequest](the_plaid_api/models/transactions_enhance_get_request.py) \| [TransactionsEnhanceGetRequestDict](the_plaid_api/models/transactions_enhance_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsEnhanceGetResponse](the_plaid_api/models/transactions_enhance_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsEnhanceGetResponse](the_plaid_api/models/transactions_enhance_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_enrich(body: TransactionsEnrichRequest | TransactionsEnrichRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsEnrichResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transactions/enrich` endpoint enriches raw transaction data generated by your own banking products or retrieved from other non-Plaid sources.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_enrich(
    TransactionsEnrichRequest(
        account_type="some example string",
        transactions=[
            ClientProvidedTransaction(
                id="some example string",
                description="some example string",
                amount=1.5,
                direction=EnrichTransactionDirection.INFLOW,
                iso_currency_code="some example string",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsEnrichResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_enrich(
    TransactionsEnrichRequest(
        account_type="some example string",
        transactions=[
            ClientProvidedTransaction(
                id="some example string",
                description="some example string",
                amount=1.5,
                direction=EnrichTransactionDirection.INFLOW,
                iso_currency_code="some example string",
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsEnrichResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsEnrichRequest](the_plaid_api/models/transactions_enrich_request.py) \| [TransactionsEnrichRequestDict](the_plaid_api/models/transactions_enrich_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsEnrichResponse](the_plaid_api/models/transactions_enrich_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsEnrichResponse](the_plaid_api/models/transactions_enrich_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_get(body: TransactionsGetRequest | TransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Note: All new implementations are encouraged to use `/transactions/sync` rather than `/transactions/get`. `/transactions/sync` provides the same functionality as `/transactions/get` and improves developer ease-of-use for handling transactions updates.
The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student` or `mortgage`; coverage may be limited). For transaction history from investment accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.
Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).
Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.
Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. To find out when the Item was last updated, use the [Item Debugger](https://plaid.com/docs/account/activity/#troubleshooting-with-item-debugger) or call `/item/get`; the `item.status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.

Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the https://plaid.com/docs/api/products/transactions/#initial_update and https://plaid.com/docs/api/products/transactions/#historical_update webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_get(
    TransactionsGetRequest(access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_get(
    TransactionsGetRequest(access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15))
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsGetRequest](the_plaid_api/models/transactions_get_request.py) \| [TransactionsGetRequestDict](the_plaid_api/models/transactions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsGetResponse](the_plaid_api/models/transactions_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsGetResponse](the_plaid_api/models/transactions_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_recurring_get(body: TransactionsRecurringGetRequest | TransactionsRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsRecurringGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user's checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.

This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/transactions/get` or `/transactions/sync`).

When using Recurring Transactions, for best results, make sure to use the https://plaid.com/docs/api/link/#link-token-create-request-transactions-days-requested parameter to request at least 180 days of history when initializing Items with Transactions. Once all historical transactions have been fetched, call `/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the https://plaid.com/docs/api/products/transactions/#recurring_transactions_update webhook. To know when historical transactions have been fetched, if you are using `/transactions/sync` listen for the https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/transactions/get`, listen for the https://plaid.com/docs/api/products/transactions/#historical_update webhook.

After the initial call, you can call the `/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the https://plaid.com/docs/api/products/transactions/#recurring_transactions_update webhook to be notified when new updates are available.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_recurring_get(
    TransactionsRecurringGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRecurringGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_recurring_get(
    TransactionsRecurringGetRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRecurringGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsRecurringGetRequest](the_plaid_api/models/transactions_recurring_get_request.py) \| [TransactionsRecurringGetRequestDict](the_plaid_api/models/transactions_recurring_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsRecurringGetResponse](the_plaid_api/models/transactions_recurring_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsRecurringGetResponse](the_plaid_api/models/transactions_recurring_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_refresh(body: TransactionsRefreshRequest | TransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/transactions/refresh` is an optional endpoint that initiates an on-demand extraction to fetch the newest transactions for an Item. The on-demand extraction takes place in addition to the periodic extractions that automatically occur one or more times per day for any Transactions-enabled Item. The Item must already have Transactions added as a product in order to call `/transactions/refresh`.

If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, https://plaid.com/docs/api/products/transactions/#sync_updates_available will be fired if there are any transactions updated, added, or removed. For users of both `/transactions/sync` and `/transactions/get`, https://plaid.com/docs/api/products/transactions/#transactions_removed will be fired if any removed transactions are detected, and https://plaid.com/docs/api/products/transactions/#default_update will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get` or `/transactions/sync`.

Note that the `/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) non-depository accounts and will result in a `PRODUCTS_NOT_SUPPORTED` error if called on an Item that contains only non-depository accounts from that institution.

As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints (typically less than 10 seconds, but occasionally up to 30 seconds or more); if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

`/transactions/refresh` is offered as an optional add-on to Transactions and has a separate [fee model](https://plaid.com/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_refresh(TransactionsRefreshRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_refresh(
    TransactionsRefreshRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsRefreshRequest](the_plaid_api/models/transactions_refresh_request.py) \| [TransactionsRefreshRequestDict](the_plaid_api/models/transactions_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsRefreshResponse](the_plaid_api/models/transactions_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsRefreshResponse](the_plaid_api/models/transactions_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_rules_create(body: TransactionsRulesCreateRequest | TransactionsRulesCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsRulesCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/transactions/rules/v1/create` endpoint creates transaction categorization rules.

Rules will be applied on the Item's transactions returned in `/transactions/get` response.

The product is currently in beta. To request access, contact transactions-feedback@plaid.com.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_rules_create(
    TransactionsRulesCreateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        client_user_id="your-client-user-id",
        pfc_primary_category="FOOD_AND_DRINK",
        pfc_detailed_category="FOOD_AND_DRINK_FAST_FOOD",
        rule_details=TransactionsRuleDetails(
            field=TransactionsRuleField.MERCHANT_NAME, type_=TransactionsRuleType.SUBSTRING_MATCH, query="Burger Shack"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRulesCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_rules_create(
    TransactionsRulesCreateRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        client_user_id="your-client-user-id",
        pfc_primary_category="FOOD_AND_DRINK",
        pfc_detailed_category="FOOD_AND_DRINK_FAST_FOOD",
        rule_details=TransactionsRuleDetails(
            field=TransactionsRuleField.MERCHANT_NAME, type_=TransactionsRuleType.SUBSTRING_MATCH, query="Burger Shack"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRulesCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsRulesCreateRequest](the_plaid_api/models/transactions_rules_create_request.py) \| [TransactionsRulesCreateRequestDict](the_plaid_api/models/transactions_rules_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsRulesCreateResponse](the_plaid_api/models/transactions_rules_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsRulesCreateResponse](the_plaid_api/models/transactions_rules_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_rules_list(body: TransactionsRulesListRequest | TransactionsRulesListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsRulesListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/transactions/rules/v1/list` returns a list of transaction rules created for the Item associated with the access token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_rules_list(
    TransactionsRulesListRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        client_user_id="your-client-user-id",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRulesListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_rules_list(
    TransactionsRulesListRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        client_user_id="your-client-user-id",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRulesListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsRulesListRequest](the_plaid_api/models/transactions_rules_list_request.py) \| [TransactionsRulesListRequestDict](the_plaid_api/models/transactions_rules_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsRulesListResponse](the_plaid_api/models/transactions_rules_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsRulesListResponse](the_plaid_api/models/transactions_rules_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_rules_remove(body: TransactionsRulesRemoveRequest | TransactionsRulesRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsRulesRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/transactions/rules/v1/remove` endpoint is used to remove a transaction rule.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_rules_remove(
    TransactionsRulesRemoveRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        client_user_id="your-client-user-id",
        rule_id="eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRulesRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_rules_remove(
    TransactionsRulesRemoveRequest(
        client_id="7f57eb3d2a9j6480121fx361",
        secret="79g03eoofwl8240v776r2h667442119",
        client_user_id="your-client-user-id",
        rule_id="eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsRulesRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsRulesRemoveRequest](the_plaid_api/models/transactions_rules_remove_request.py) \| [TransactionsRulesRemoveRequestDict](the_plaid_api/models/transactions_rules_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsRulesRemoveResponse](the_plaid_api/models/transactions_rules_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsRulesRemoveResponse](the_plaid_api/models/transactions_rules_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_sync(body: TransactionsSyncRequest | TransactionsSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsSyncResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transactions/sync` endpoint retrieves transactions associated with an Item and can fetch updates using a cursor to track which updates have already been seen.

For important instructions on integrating with `/transactions/sync`, see the [Transactions integration overview](https://plaid.com/docs/transactions/#integration-overview). If you are migrating from an existing integration using `/transactions/get`, see the [Transactions Sync migration guide](https://plaid.com/docs/transactions/sync-migration/).

This endpoint supports `credit`, `depository`, and some `loan`-type accounts (only those with account subtype `student` or `mortgage`). For `investments` accounts, use `/investments/transactions/get` instead.

When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/transactions/sync` fails when retrieving a paginated update (e.g. due to the https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination error), the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.

If transactions data is not yet available for the Item, which can happen if the Item was not initialized with transactions during the `/link/token/create` call or if `/transactions/sync` was called within a few seconds of Item creation, `/transactions/sync` will return empty transactions arrays.

Plaid typically checks for new transactions data between one and four times per day, depending on the institution. To find out when transactions were last updated for an Item, use the [Item Debugger](https://plaid.com/docs/account/activity/#troubleshooting-with-item-debugger) or call `/item/get`; the `item.status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/transactions/refresh` endpoint.

To be alerted when new transactions are available, listen for the https://plaid.com/docs/api/products/transactions/#sync_updates_available webhook.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_sync(TransactionsSyncRequest(access_token="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_sync(
    TransactionsSyncRequest(access_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsSyncRequest](the_plaid_api/models/transactions_sync_request.py) \| [TransactionsSyncRequestDict](the_plaid_api/models/transactions_sync_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsSyncResponse](the_plaid_api/models/transactions_sync_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsSyncResponse](the_plaid_api/models/transactions_sync_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_user_insights_get(body: TransactionsUserInsightsGetRequest | TransactionsUserInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionsUserInsightsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/beta/transactions/user_insights/v1/get` gets user insights for clients who have enriched data with `/transactions/enrich`.

The product is currently in beta.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transactions_user_insights_get(
    TransactionsUserInsightsGetRequest(client_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsUserInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transactions_user_insights_get(
    TransactionsUserInsightsGetRequest(client_user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionsUserInsightsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsUserInsightsGetRequest](the_plaid_api/models/transactions_user_insights_get_request.py) \| [TransactionsUserInsightsGetRequestDict](the_plaid_api/models/transactions_user_insights_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransactionsUserInsightsGetResponse](the_plaid_api/models/transactions_user_insights_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionsUserInsightsGetResponse](the_plaid_api/models/transactions_user_insights_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_authorization_cancel(body: TransferAuthorizationCancelRequest | TransferAuthorizationCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferAuthorizationCancelResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/authorization/cancel` endpoint to cancel a transfer authorization. A transfer authorization is eligible for cancellation if it has not yet been used to create a transfer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_authorization_cancel(
    TransferAuthorizationCancelRequest(authorization_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferAuthorizationCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_authorization_cancel(
    TransferAuthorizationCancelRequest(authorization_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferAuthorizationCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferAuthorizationCancelRequest](the_plaid_api/models/transfer_authorization_cancel_request.py) \| [TransferAuthorizationCancelRequestDict](the_plaid_api/models/transfer_authorization_cancel_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferAuthorizationCancelResponse](the_plaid_api/models/transfer_authorization_cancel_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferAuthorizationCancelResponse](the_plaid_api/models/transfer_authorization_cancel_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_authorization_create(body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferAuthorizationCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/authorization/create` endpoint to authorize a transfer. This endpoint must be called prior to calling `/transfer/create`. The transfer authorization will expire if not used after one hour. (You can contact your account manager to change the default authorization lifetime.)

There are four possible outcomes to calling this endpoint:

  - If the `authorization.decision` in the response is `declined`, the proposed transfer has failed the risk check and you cannot proceed with the transfer.

  - If the `authorization.decision` is `user_action_required`, additional user input is needed, usually to fix a broken bank connection, before Plaid can properly assess the risk. You need to launch Link in update mode to complete the required user action. When calling `/link/token/create` to get a new Link token, instead of providing `access_token` in the request, you should set https://plaid.com/docs/api/link/#link-token-create-request-transfer-authorization-id as the `authorization.id`. After the Link flow is completed, you may re-attempt the authorization.

  - If the `authorization.decision` is `approved`, and the `authorization.decision_rationale.code` is `null`, the transfer has passed the risk check and you can proceed to call `/transfer/create`.

  - If the `authorization.decision` is `approved` and the `authorization.decision_rationale.code` is non-`null`, the risk check could not be run: you may proceed with the transfer, but should perform your own risk evaluation. For more details, see the response schema.

In Plaid's Sandbox environment the decisions will be returned as follows:

  - To approve a transfer with `null` rationale code, make an authorization request with an `amount` less than the available balance in the account.

  - To approve a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same-Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).

  - To get an authorization decision of `user_action_required`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).

  - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

  - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_authorization_create(
    TransferAuthorizationCreateRequest(
        access_token="some example string",
        account_id="some example string",
        type_=TransferType.DEBIT,
        network=TransferNetwork.ACH,
        amount="some example string",
        user=TransferAuthorizationUserInRequest(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferAuthorizationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_authorization_create(
    TransferAuthorizationCreateRequest(
        access_token="some example string",
        account_id="some example string",
        type_=TransferType.DEBIT,
        network=TransferNetwork.ACH,
        amount="some example string",
        user=TransferAuthorizationUserInRequest(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferAuthorizationCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferAuthorizationCreateRequest](the_plaid_api/models/transfer_authorization_create_request.py) \| [TransferAuthorizationCreateRequestDict](the_plaid_api/models/transfer_authorization_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferAuthorizationCreateResponse](the_plaid_api/models/transfer_authorization_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferAuthorizationCreateResponse](the_plaid_api/models/transfer_authorization_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_balance_get(body: TransferBalanceGetRequest | TransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferBalanceGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

(Deprecated) Use the `/transfer/ledger/get` endpoint to view a balance held with Plaid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_balance_get(TransferBalanceGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferBalanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_balance_get(TransferBalanceGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferBalanceGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferBalanceGetRequest](the_plaid_api/models/transfer_balance_get_request.py) \| [TransferBalanceGetRequestDict](the_plaid_api/models/transfer_balance_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferBalanceGetResponse](the_plaid_api/models/transfer_balance_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferBalanceGetResponse](the_plaid_api/models/transfer_balance_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_cancel(body: TransferCancelRequest | TransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferCancelResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancellation if the `cancellable` property returned by `/transfer/get` is `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_cancel(TransferCancelRequest(transfer_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_cancel(TransferCancelRequest(transfer_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferCancelRequest](the_plaid_api/models/transfer_cancel_request.py) \| [TransferCancelRequestDict](the_plaid_api/models/transfer_cancel_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferCancelResponse](the_plaid_api/models/transfer_cancel_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferCancelResponse](the_plaid_api/models/transfer_cancel_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_capabilities_get(body: TransferCapabilitiesGetRequest | TransferCapabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferCapabilitiesGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/capabilities/get` endpoint to determine the RTP eligibility information of an account to be used with Transfer. This endpoint works on all Transfer-capable Items, including those created by `/transfer/migrate_account`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_capabilities_get(
    TransferCapabilitiesGetRequest(access_token="some example string", account_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferCapabilitiesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_capabilities_get(
    TransferCapabilitiesGetRequest(access_token="some example string", account_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferCapabilitiesGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferCapabilitiesGetRequest](the_plaid_api/models/transfer_capabilities_get_request.py) \| [TransferCapabilitiesGetRequestDict](the_plaid_api/models/transfer_capabilities_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferCapabilitiesGetResponse](the_plaid_api/models/transfer_capabilities_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferCapabilitiesGetResponse](the_plaid_api/models/transfer_capabilities_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_configuration_get(body: TransferConfigurationGetRequest | TransferConfigurationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferConfigurationGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/configuration/get` endpoint to view your transfer product configurations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_configuration_get(TransferConfigurationGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferConfigurationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_configuration_get(TransferConfigurationGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferConfigurationGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferConfigurationGetRequest](the_plaid_api/models/transfer_configuration_get_request.py) \| [TransferConfigurationGetRequestDict](the_plaid_api/models/transfer_configuration_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferConfigurationGetResponse](the_plaid_api/models/transfer_configuration_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferConfigurationGetResponse](the_plaid_api/models/transfer_configuration_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_create(body: TransferCreateRequest | TransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/create` endpoint to initiate a new transfer. This endpoint is retryable and idempotent; if a transfer with the provided `transfer_id` has already been created, it will return the transfer details without creating a new transfer. A transfer may still be created if a 500 error is returned; to detect this scenario, use [Transfer events](https://plaid.com/docs/transfer/reconciling-transfers/).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_create(
    TransferCreateRequest(
        access_token="some example string",
        account_id="some example string",
        authorization_id="some example string",
        description="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_create(
    TransferCreateRequest(
        access_token="some example string",
        account_id="some example string",
        authorization_id="some example string",
        description="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferCreateRequest](the_plaid_api/models/transfer_create_request.py) \| [TransferCreateRequestDict](the_plaid_api/models/transfer_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferCreateResponse](the_plaid_api/models/transfer_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferCreateResponse](the_plaid_api/models/transfer_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_diligence_document_upload(body: TransferDiligenceDocumentUploadRequest | TransferDiligenceDocumentUploadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferDiligenceDocumentUploadResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Third-party sender customers can use the `/transfer/diligence/document/upload` endpoint to upload a document on behalf of their end customer (i.e. originator) to Plaid. You'll need to send a request of type `multipart/form-data`.
You must provide the `client_id` in the `PLAID-CLIENT-ID` header and `secret` in the `PLAID-SECRET` header.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_diligence_document_upload(
    TransferDiligenceDocumentUploadRequest(
        originator_client_id="some example string", file=Path("path/to/file.bin"), purpose=Purpose.DUE_DILIGENCE
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferDiligenceDocumentUploadResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_diligence_document_upload(
    TransferDiligenceDocumentUploadRequest(
        originator_client_id="some example string", file=Path("path/to/file.bin"), purpose=Purpose.DUE_DILIGENCE
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferDiligenceDocumentUploadResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferDiligenceDocumentUploadRequest](the_plaid_api/models/transfer_diligence_document_upload_request.py) \| [TransferDiligenceDocumentUploadRequestDict](the_plaid_api/models/transfer_diligence_document_upload_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferDiligenceDocumentUploadResponse](the_plaid_api/models/transfer_diligence_document_upload_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferDiligenceDocumentUploadResponse](the_plaid_api/models/transfer_diligence_document_upload_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_diligence_submit(body: TransferDiligenceSubmitRequest | TransferDiligenceSubmitRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferDiligenceSubmitResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/diligence/submit` endpoint to submit transfer diligence on behalf of the originator (i.e., the end customer).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_diligence_submit(
    TransferDiligenceSubmitRequest(
        originator_client_id="some example string",
        originator_diligence=TransferOriginatorDiligence(
            dba="some example string",
            tax_id="some example string",
            address=TransferOriginatorAddress(
                city="some example string",
                street="some example string",
                region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            website="some example string",
            naics_code="some example string",
            funding_account=TransferFundingAccount(
                access_token="some example string", account_id="some example string"
            ),
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferDiligenceSubmitResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_diligence_submit(
    TransferDiligenceSubmitRequest(
        originator_client_id="some example string",
        originator_diligence=TransferOriginatorDiligence(
            dba="some example string",
            tax_id="some example string",
            address=TransferOriginatorAddress(
                city="some example string",
                street="some example string",
                region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            website="some example string",
            naics_code="some example string",
            funding_account=TransferFundingAccount(
                access_token="some example string", account_id="some example string"
            ),
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferDiligenceSubmitResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferDiligenceSubmitRequest](the_plaid_api/models/transfer_diligence_submit_request.py) \| [TransferDiligenceSubmitRequestDict](the_plaid_api/models/transfer_diligence_submit_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferDiligenceSubmitResponse](the_plaid_api/models/transfer_diligence_submit_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferDiligenceSubmitResponse](the_plaid_api/models/transfer_diligence_submit_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_event_list(body: TransferEventListRequest | TransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferEventListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_event_list(TransferEventListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferEventListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_event_list(TransferEventListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferEventListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferEventListRequest](the_plaid_api/models/transfer_event_list_request.py) \| [TransferEventListRequestDict](the_plaid_api/models/transfer_event_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferEventListResponse](the_plaid_api/models/transfer_event_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferEventListResponse](the_plaid_api/models/transfer_event_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_event_sync(body: TransferEventSyncRequest | TransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferEventSyncResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/transfer/event/sync` allows you to request up to the next 500 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_event_sync(TransferEventSyncRequest(after_id=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferEventSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_event_sync(TransferEventSyncRequest(after_id=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferEventSyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferEventSyncRequest](the_plaid_api/models/transfer_event_sync_request.py) \| [TransferEventSyncRequestDict](the_plaid_api/models/transfer_event_sync_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferEventSyncResponse](the_plaid_api/models/transfer_event_sync_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferEventSyncResponse](the_plaid_api/models/transfer_event_sync_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_get(body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/get` endpoint fetches information about the transfer corresponding to the given `transfer_id` or `authorization_id`. One of `transfer_id` or `authorization_id` must be populated but not both.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_get(TransferGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_get(TransferGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferGetRequest](the_plaid_api/models/transfer_get_request.py) \| [TransferGetRequestDict](the_plaid_api/models/transfer_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferGetResponse](the_plaid_api/models/transfer_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferGetResponse](the_plaid_api/models/transfer_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_intent_create(body: TransferIntentCreateRequest | TransferIntentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferIntentCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/intent/create` endpoint to generate a transfer intent object and invoke the Transfer UI.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_intent_create(
    TransferIntentCreateRequest(
        mode=TransferIntentCreateMode.PAYMENT,
        amount="some example string",
        description="some example string",
        user=TransferUserInRequest(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferIntentCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_intent_create(
    TransferIntentCreateRequest(
        mode=TransferIntentCreateMode.PAYMENT,
        amount="some example string",
        description="some example string",
        user=TransferUserInRequest(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferIntentCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferIntentCreateRequest](the_plaid_api/models/transfer_intent_create_request.py) \| [TransferIntentCreateRequestDict](the_plaid_api/models/transfer_intent_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferIntentCreateResponse](the_plaid_api/models/transfer_intent_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferIntentCreateResponse](the_plaid_api/models/transfer_intent_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_intent_get(body: TransferIntentGetRequest | TransferIntentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferIntentGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/intent/get` endpoint to retrieve more information about a transfer intent.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_intent_get(
    TransferIntentGetRequest(transfer_intent_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferIntentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_intent_get(
    TransferIntentGetRequest(transfer_intent_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferIntentGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferIntentGetRequest](the_plaid_api/models/transfer_intent_get_request.py) \| [TransferIntentGetRequestDict](the_plaid_api/models/transfer_intent_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferIntentGetResponse](the_plaid_api/models/transfer_intent_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferIntentGetResponse](the_plaid_api/models/transfer_intent_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_deposit(body: TransferLedgerDepositRequest | TransferLedgerDepositRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferLedgerDepositResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/ledger/deposit` endpoint to deposit funds into Plaid Ledger.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_ledger_deposit(
    TransferLedgerDepositRequest(
        amount="some example string", idempotency_key="some example string", network=TransferAchnetwork.ACH
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerDepositResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_ledger_deposit(
    TransferLedgerDepositRequest(
        amount="some example string", idempotency_key="some example string", network=TransferAchnetwork.ACH
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerDepositResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferLedgerDepositRequest](the_plaid_api/models/transfer_ledger_deposit_request.py) \| [TransferLedgerDepositRequestDict](the_plaid_api/models/transfer_ledger_deposit_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferLedgerDepositResponse](the_plaid_api/models/transfer_ledger_deposit_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferLedgerDepositResponse](the_plaid_api/models/transfer_ledger_deposit_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_distribute(body: TransferLedgerDistributeRequest | TransferLedgerDistributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferLedgerDistributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/ledger/distribute` endpoint to move available balance between ledgers, if you have multiple. If you're a platform, you can move funds between one of your ledgers and one of your customer's ledgers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_ledger_distribute(
    TransferLedgerDistributeRequest(
        from_ledger_id="some example string",
        to_ledger_id="some example string",
        amount="some example string",
        idempotency_key="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerDistributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_ledger_distribute(
    TransferLedgerDistributeRequest(
        from_ledger_id="some example string",
        to_ledger_id="some example string",
        amount="some example string",
        idempotency_key="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerDistributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferLedgerDistributeRequest](the_plaid_api/models/transfer_ledger_distribute_request.py) \| [TransferLedgerDistributeRequestDict](the_plaid_api/models/transfer_ledger_distribute_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferLedgerDistributeResponse](the_plaid_api/models/transfer_ledger_distribute_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferLedgerDistributeResponse](the_plaid_api/models/transfer_ledger_distribute_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_event_list(body: TransferLedgerEventListRequest | TransferLedgerEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferLedgerEventListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/ledger/event/list` endpoint to get a list of ledger events for a specific ledger based on specified filter criteria.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_ledger_event_list(TransferLedgerEventListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerEventListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_ledger_event_list(TransferLedgerEventListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerEventListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferLedgerEventListRequest](the_plaid_api/models/transfer_ledger_event_list_request.py) \| [TransferLedgerEventListRequestDict](the_plaid_api/models/transfer_ledger_event_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferLedgerEventListResponse](the_plaid_api/models/transfer_ledger_event_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferLedgerEventListResponse](the_plaid_api/models/transfer_ledger_event_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_get(body: TransferLedgerGetRequest | TransferLedgerGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferLedgerGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/ledger/get` endpoint to view a balance on the ledger held with Plaid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_ledger_get(TransferLedgerGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_ledger_get(TransferLedgerGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferLedgerGetRequest](the_plaid_api/models/transfer_ledger_get_request.py) \| [TransferLedgerGetRequestDict](the_plaid_api/models/transfer_ledger_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferLedgerGetResponse](the_plaid_api/models/transfer_ledger_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferLedgerGetResponse](the_plaid_api/models/transfer_ledger_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_withdraw(body: TransferLedgerWithdrawRequest | TransferLedgerWithdrawRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferLedgerWithdrawResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/ledger/withdraw` endpoint to withdraw funds from a Plaid Ledger balance.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_ledger_withdraw(
    TransferLedgerWithdrawRequest(
        amount="some example string", idempotency_key="some example string", network=TransferNetwork.ACH
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerWithdrawResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_ledger_withdraw(
    TransferLedgerWithdrawRequest(
        amount="some example string", idempotency_key="some example string", network=TransferNetwork.ACH
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferLedgerWithdrawResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferLedgerWithdrawRequest](the_plaid_api/models/transfer_ledger_withdraw_request.py) \| [TransferLedgerWithdrawRequestDict](the_plaid_api/models/transfer_ledger_withdraw_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferLedgerWithdrawResponse](the_plaid_api/models/transfer_ledger_withdraw_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferLedgerWithdrawResponse](the_plaid_api/models/transfer_ledger_withdraw_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_list(body: TransferListRequest | TransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_list(TransferListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_list(TransferListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferListRequest](the_plaid_api/models/transfer_list_request.py) \| [TransferListRequestDict](the_plaid_api/models/transfer_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferListResponse](the_plaid_api/models/transfer_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferListResponse](the_plaid_api/models/transfer_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_metrics_get(body: TransferMetricsGetRequest | TransferMetricsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferMetricsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/metrics/get` endpoint to view your transfer product usage metrics.

In the Sandbox environment, this endpoint returns static placeholder values rather than metrics computed from your Sandbox transfer activity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_metrics_get(TransferMetricsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferMetricsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_metrics_get(TransferMetricsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferMetricsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferMetricsGetRequest](the_plaid_api/models/transfer_metrics_get_request.py) \| [TransferMetricsGetRequestDict](the_plaid_api/models/transfer_metrics_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferMetricsGetResponse](the_plaid_api/models/transfer_metrics_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferMetricsGetResponse](the_plaid_api/models/transfer_metrics_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_migrate_account(body: TransferMigrateAccountRequest | TransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferMigrateAccountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate previously-verified account and routing numbers to Plaid Items. This endpoint is also required when adding an Item for use with wire transfers; if you intend to create wire transfers on this account, you must provide `wire_routing_number`. Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid account manager or [support](https://dashboard.plaid.com/support).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_migrate_account(
    TransferMigrateAccountRequest(
        account_number="some example string", routing_number="some example string", account_type="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferMigrateAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_migrate_account(
    TransferMigrateAccountRequest(
        account_number="some example string", routing_number="some example string", account_type="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferMigrateAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferMigrateAccountRequest](the_plaid_api/models/transfer_migrate_account_request.py) \| [TransferMigrateAccountRequestDict](the_plaid_api/models/transfer_migrate_account_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferMigrateAccountResponse](the_plaid_api/models/transfer_migrate_account_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferMigrateAccountResponse](the_plaid_api/models/transfer_migrate_account_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_create(body: TransferOriginatorCreateRequest | TransferOriginatorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferOriginatorCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/originator/create` endpoint to create a new originator and return an `originator_client_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_originator_create(
    TransferOriginatorCreateRequest(company_name="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_originator_create(
    TransferOriginatorCreateRequest(company_name="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferOriginatorCreateRequest](the_plaid_api/models/transfer_originator_create_request.py) \| [TransferOriginatorCreateRequestDict](the_plaid_api/models/transfer_originator_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferOriginatorCreateResponse](the_plaid_api/models/transfer_originator_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferOriginatorCreateResponse](the_plaid_api/models/transfer_originator_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_funding_account_create(body: TransferOriginatorFundingAccountCreateRequest | TransferOriginatorFundingAccountCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferOriginatorFundingAccountCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/originator/funding_account/create` endpoint to create a new funding account for the originator.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_originator_funding_account_create(
    TransferOriginatorFundingAccountCreateRequest(
        originator_client_id="some example string",
        funding_account=TransferFundingAccountWithDisplayName(
            access_token="some example string", account_id="some example string"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorFundingAccountCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_originator_funding_account_create(
    TransferOriginatorFundingAccountCreateRequest(
        originator_client_id="some example string",
        funding_account=TransferFundingAccountWithDisplayName(
            access_token="some example string", account_id="some example string"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorFundingAccountCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferOriginatorFundingAccountCreateRequest](the_plaid_api/models/transfer_originator_funding_account_create_request.py) \| [TransferOriginatorFundingAccountCreateRequestDict](the_plaid_api/models/transfer_originator_funding_account_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferOriginatorFundingAccountCreateResponse](the_plaid_api/models/transfer_originator_funding_account_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferOriginatorFundingAccountCreateResponse](the_plaid_api/models/transfer_originator_funding_account_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_funding_account_update(body: TransferOriginatorFundingAccountUpdateRequest | TransferOriginatorFundingAccountUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferOriginatorFundingAccountUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/originator/funding_account/update` endpoint to update the funding account associated with the originator.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_originator_funding_account_update(
    TransferOriginatorFundingAccountUpdateRequest(
        originator_client_id="some example string",
        funding_account=TransferFundingAccount(access_token="some example string", account_id="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorFundingAccountUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_originator_funding_account_update(
    TransferOriginatorFundingAccountUpdateRequest(
        originator_client_id="some example string",
        funding_account=TransferFundingAccount(access_token="some example string", account_id="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorFundingAccountUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferOriginatorFundingAccountUpdateRequest](the_plaid_api/models/transfer_originator_funding_account_update_request.py) \| [TransferOriginatorFundingAccountUpdateRequestDict](the_plaid_api/models/transfer_originator_funding_account_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferOriginatorFundingAccountUpdateResponse](the_plaid_api/models/transfer_originator_funding_account_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferOriginatorFundingAccountUpdateResponse](the_plaid_api/models/transfer_originator_funding_account_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_get(body: TransferOriginatorGetRequest | TransferOriginatorGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferOriginatorGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/originator/get` endpoint gets status updates for an originator's onboarding process. This information is also available via the Transfer page on the Plaid dashboard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_originator_get(
    TransferOriginatorGetRequest(originator_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_originator_get(
    TransferOriginatorGetRequest(originator_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferOriginatorGetRequest](the_plaid_api/models/transfer_originator_get_request.py) \| [TransferOriginatorGetRequestDict](the_plaid_api/models/transfer_originator_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferOriginatorGetResponse](the_plaid_api/models/transfer_originator_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferOriginatorGetResponse](the_plaid_api/models/transfer_originator_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_list(body: TransferOriginatorListRequest | TransferOriginatorListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferOriginatorListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/originator/list` endpoint gets status updates for all of your originators' onboarding. This information is also available via the Plaid dashboard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_originator_list(TransferOriginatorListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_originator_list(TransferOriginatorListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferOriginatorListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferOriginatorListRequest](the_plaid_api/models/transfer_originator_list_request.py) \| [TransferOriginatorListRequestDict](the_plaid_api/models/transfer_originator_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferOriginatorListResponse](the_plaid_api/models/transfer_originator_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferOriginatorListResponse](the_plaid_api/models/transfer_originator_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_platform_originator_create(body: TransferPlatformOriginatorCreateRequest | TransferPlatformOriginatorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferPlatformOriginatorCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/platform/originator/create` endpoint to submit information about the originator you are onboarding, including the originator's agreement to the required legal terms.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_platform_originator_create(
    TransferPlatformOriginatorCreateRequest(
        originator_client_id="some example string",
        tos_acceptance_metadata=TosacceptanceMetadata(
            agreement_accepted=True,
            originator_ip_address="some example string",
            agreement_accepted_at=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
        ),
        originator_reviewed_at=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferPlatformOriginatorCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_platform_originator_create(
    TransferPlatformOriginatorCreateRequest(
        originator_client_id="some example string",
        tos_acceptance_metadata=TosacceptanceMetadata(
            agreement_accepted=True,
            originator_ip_address="some example string",
            agreement_accepted_at=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
        ),
        originator_reviewed_at=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferPlatformOriginatorCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferPlatformOriginatorCreateRequest](the_plaid_api/models/transfer_platform_originator_create_request.py) \| [TransferPlatformOriginatorCreateRequestDict](the_plaid_api/models/transfer_platform_originator_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferPlatformOriginatorCreateResponse](the_plaid_api/models/transfer_platform_originator_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferPlatformOriginatorCreateResponse](the_plaid_api/models/transfer_platform_originator_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_platform_person_create(body: TransferPlatformPersonCreateRequest | TransferPlatformPersonCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferPlatformPersonCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/platform/person/create` endpoint to create a person associated with an originator (e.g. beneficial owner or control person) and optionally submit personal identification information for them.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_platform_person_create(
    TransferPlatformPersonCreateRequest(originator_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferPlatformPersonCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_platform_person_create(
    TransferPlatformPersonCreateRequest(originator_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferPlatformPersonCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferPlatformPersonCreateRequest](the_plaid_api/models/transfer_platform_person_create_request.py) \| [TransferPlatformPersonCreateRequestDict](the_plaid_api/models/transfer_platform_person_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferPlatformPersonCreateResponse](the_plaid_api/models/transfer_platform_person_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferPlatformPersonCreateResponse](the_plaid_api/models/transfer_platform_person_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_platform_requirement_submit(body: TransferPlatformRequirementSubmitRequest | TransferPlatformRequirementSubmitRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferPlatformRequirementSubmitResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/platform/requirement/submit` endpoint to submit additional onboarding information that is needed by Plaid to approve or decline the originator. See [Requirement type schema documentation](https://docs.google.com/document/d/1NEQkTD0sVK50iAQi6xHigrexDUxZ4QxXqSEfV_FFTiU/) for a list of requirement types and possible values.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_platform_requirement_submit(
    TransferPlatformRequirementSubmitRequest(
        originator_client_id="some example string",
        requirement_submissions=[
            RequirementSubmission(requirement_type="some example string", value="some example string")
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferPlatformRequirementSubmitResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_platform_requirement_submit(
    TransferPlatformRequirementSubmitRequest(
        originator_client_id="some example string",
        requirement_submissions=[
            RequirementSubmission(requirement_type="some example string", value="some example string")
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferPlatformRequirementSubmitResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferPlatformRequirementSubmitRequest](the_plaid_api/models/transfer_platform_requirement_submit_request.py) \| [TransferPlatformRequirementSubmitRequestDict](the_plaid_api/models/transfer_platform_requirement_submit_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferPlatformRequirementSubmitResponse](the_plaid_api/models/transfer_platform_requirement_submit_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferPlatformRequirementSubmitResponse](the_plaid_api/models/transfer_platform_requirement_submit_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_questionnaire_create(body: TransferQuestionnaireCreateRequest | TransferQuestionnaireCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferQuestionnaireCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/questionnaire/create` endpoint generates a Plaid-hosted onboarding UI URL. Redirect the originator to this URL to provide their due diligence information and agree to Plaid's terms for ACH money movement.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_questionnaire_create(
    TransferQuestionnaireCreateRequest(originator_client_id="some example string", redirect_uri="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferQuestionnaireCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_questionnaire_create(
    TransferQuestionnaireCreateRequest(originator_client_id="some example string", redirect_uri="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferQuestionnaireCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferQuestionnaireCreateRequest](the_plaid_api/models/transfer_questionnaire_create_request.py) \| [TransferQuestionnaireCreateRequestDict](the_plaid_api/models/transfer_questionnaire_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferQuestionnaireCreateResponse](the_plaid_api/models/transfer_questionnaire_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferQuestionnaireCreateResponse](the_plaid_api/models/transfer_questionnaire_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_cancel(body: TransferRecurringCancelRequest | TransferRecurringCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRecurringCancelResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/recurring/cancel` endpoint to cancel a recurring transfer.  A scheduled transfer that hasn't been submitted to the bank will be cancelled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_recurring_cancel(
    TransferRecurringCancelRequest(recurring_transfer_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_recurring_cancel(
    TransferRecurringCancelRequest(recurring_transfer_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRecurringCancelRequest](the_plaid_api/models/transfer_recurring_cancel_request.py) \| [TransferRecurringCancelRequestDict](the_plaid_api/models/transfer_recurring_cancel_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRecurringCancelResponse](the_plaid_api/models/transfer_recurring_cancel_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRecurringCancelResponse](the_plaid_api/models/transfer_recurring_cancel_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_create(body: TransferRecurringCreateRequest | TransferRecurringCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRecurringCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/recurring/create` endpoint to initiate a new recurring transfer. This capability is not currently supported for Transfer UI or Transfer for Platforms (beta) customers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_recurring_create(
    TransferRecurringCreateRequest(
        access_token="some example string",
        idempotency_key="some example string",
        account_id="some example string",
        type_=TransferType.DEBIT,
        network=TransferRecurringNetwork.ACH,
        amount="some example string",
        description="some example string",
        schedule=TransferRecurringSchedule(
            interval_unit=TransferScheduleIntervalUnit.WEEK,
            interval_count=1,
            interval_execution_day=1,
            start_date=date(2024, 1, 15),
        ),
        user=TransferUserInRequest(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_recurring_create(
    TransferRecurringCreateRequest(
        access_token="some example string",
        idempotency_key="some example string",
        account_id="some example string",
        type_=TransferType.DEBIT,
        network=TransferRecurringNetwork.ACH,
        amount="some example string",
        description="some example string",
        schedule=TransferRecurringSchedule(
            interval_unit=TransferScheduleIntervalUnit.WEEK,
            interval_count=1,
            interval_execution_day=1,
            start_date=date(2024, 1, 15),
        ),
        user=TransferUserInRequest(legal_name="some example string"),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRecurringCreateRequest](the_plaid_api/models/transfer_recurring_create_request.py) \| [TransferRecurringCreateRequestDict](the_plaid_api/models/transfer_recurring_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRecurringCreateResponse](the_plaid_api/models/transfer_recurring_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRecurringCreateResponse](the_plaid_api/models/transfer_recurring_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_get(body: TransferRecurringGetRequest | TransferRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRecurringGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/recurring/get` fetches information about the recurring transfer corresponding to the given `recurring_transfer_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_recurring_get(
    TransferRecurringGetRequest(recurring_transfer_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_recurring_get(
    TransferRecurringGetRequest(recurring_transfer_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRecurringGetRequest](the_plaid_api/models/transfer_recurring_get_request.py) \| [TransferRecurringGetRequestDict](the_plaid_api/models/transfer_recurring_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRecurringGetResponse](the_plaid_api/models/transfer_recurring_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRecurringGetResponse](the_plaid_api/models/transfer_recurring_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_list(body: TransferRecurringListRequest | TransferRecurringListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRecurringListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/recurring/list` endpoint to see a list of all your recurring transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired recurring transfers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_recurring_list(TransferRecurringListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_recurring_list(TransferRecurringListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRecurringListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRecurringListRequest](the_plaid_api/models/transfer_recurring_list_request.py) \| [TransferRecurringListRequestDict](the_plaid_api/models/transfer_recurring_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRecurringListResponse](the_plaid_api/models/transfer_recurring_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRecurringListResponse](the_plaid_api/models/transfer_recurring_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_refund_cancel(body: TransferRefundCancelRequest | TransferRefundCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRefundCancelResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/refund/cancel` endpoint to cancel a refund.  A refund is eligible for cancellation if it has not yet been submitted to the payment network.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_refund_cancel(TransferRefundCancelRequest(refund_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRefundCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_refund_cancel(
    TransferRefundCancelRequest(refund_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRefundCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRefundCancelRequest](the_plaid_api/models/transfer_refund_cancel_request.py) \| [TransferRefundCancelRequestDict](the_plaid_api/models/transfer_refund_cancel_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRefundCancelResponse](the_plaid_api/models/transfer_refund_cancel_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRefundCancelResponse](the_plaid_api/models/transfer_refund_cancel_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_refund_create(body: TransferRefundCreateRequest | TransferRefundCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRefundCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/refund/create` endpoint to create a refund for a transfer. A transfer can be refunded if the transfer was initiated in the past 180 days.

Refunds come out of the available balance of the ledger used for the original debit transfer. If there are not enough funds in the available balance to cover the refund amount, the refund will be rejected. You can create a refund at any time. Plaid does not impose any hold time on refunds.

A refund can still be issued even if the Item's `access_token` is no longer valid (e.g. if the user revoked OAuth consent or the Item was deleted via `/item/remove`), as long as the account and routing number pair used to make the original transaction is still valid. A refund cannot be issued if the Item has an [invalidated TAN](https://plaid.com/docs/auth/#tokenized-account-numbers), which can occur at Chase or PNC.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_refund_create(
    TransferRefundCreateRequest(
        transfer_id="some example string", amount="some example string", idempotency_key="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRefundCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_refund_create(
    TransferRefundCreateRequest(
        transfer_id="some example string", amount="some example string", idempotency_key="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRefundCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRefundCreateRequest](the_plaid_api/models/transfer_refund_create_request.py) \| [TransferRefundCreateRequestDict](the_plaid_api/models/transfer_refund_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRefundCreateResponse](the_plaid_api/models/transfer_refund_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRefundCreateResponse](the_plaid_api/models/transfer_refund_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_refund_get(body: TransferRefundGetRequest | TransferRefundGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRefundGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/refund/get` endpoint fetches information about the refund corresponding to the given `refund_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_refund_get(TransferRefundGetRequest(refund_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRefundGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_refund_get(
    TransferRefundGetRequest(refund_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRefundGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRefundGetRequest](the_plaid_api/models/transfer_refund_get_request.py) \| [TransferRefundGetRequestDict](the_plaid_api/models/transfer_refund_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRefundGetResponse](the_plaid_api/models/transfer_refund_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRefundGetResponse](the_plaid_api/models/transfer_refund_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_repayment_list(body: TransferRepaymentListRequest | TransferRepaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRepaymentListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/repayment/list` endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given `start_time`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_repayment_list(TransferRepaymentListRequest(count=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRepaymentListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_repayment_list(TransferRepaymentListRequest(count=1))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRepaymentListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRepaymentListRequest](the_plaid_api/models/transfer_repayment_list_request.py) \| [TransferRepaymentListRequestDict](the_plaid_api/models/transfer_repayment_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRepaymentListResponse](the_plaid_api/models/transfer_repayment_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRepaymentListResponse](the_plaid_api/models/transfer_repayment_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_repayment_return_list(body: TransferRepaymentReturnListRequest | TransferRepaymentReturnListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferRepaymentReturnListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/repayment/return/list` endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_repayment_return_list(
    TransferRepaymentReturnListRequest(repayment_id="d4bfce70-2470-4298-ae87-5e9b3e18bfaf", count=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRepaymentReturnListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_repayment_return_list(
    TransferRepaymentReturnListRequest(repayment_id="d4bfce70-2470-4298-ae87-5e9b3e18bfaf", count=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferRepaymentReturnListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferRepaymentReturnListRequest](the_plaid_api/models/transfer_repayment_return_list_request.py) \| [TransferRepaymentReturnListRequestDict](the_plaid_api/models/transfer_repayment_return_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferRepaymentReturnListResponse](the_plaid_api/models/transfer_repayment_return_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferRepaymentReturnListResponse](the_plaid_api/models/transfer_repayment_return_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_return_recover(body: TransferReturnRecoverRequest | TransferReturnRecoverRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferReturnRecoverResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/return/recover` endpoint to notify Plaid that you have recovered some or all of the loss on a returned guaranteed transfer.

Recovery can be reported in full or in parts; the sum of recovered amounts across calls cannot exceed the original transfer's amount.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_return_recover(
    TransferReturnRecoverRequest(
        transfer_id="some example string", amount="some example string", idempotency_key="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferReturnRecoverResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_return_recover(
    TransferReturnRecoverRequest(
        transfer_id="some example string", amount="some example string", idempotency_key="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferReturnRecoverResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferReturnRecoverRequest](the_plaid_api/models/transfer_return_recover_request.py) \| [TransferReturnRecoverRequestDict](the_plaid_api/models/transfer_return_recover_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferReturnRecoverResponse](the_plaid_api/models/transfer_return_recover_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferReturnRecoverResponse](the_plaid_api/models/transfer_return_recover_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_sweep_get(body: TransferSweepGetRequest | TransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferSweepGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/sweep/get` endpoint fetches a sweep corresponding to the given `sweep_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_sweep_get(TransferSweepGetRequest(sweep_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferSweepGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_sweep_get(
    TransferSweepGetRequest(sweep_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferSweepGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferSweepGetRequest](the_plaid_api/models/transfer_sweep_get_request.py) \| [TransferSweepGetRequestDict](the_plaid_api/models/transfer_sweep_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferSweepGetResponse](the_plaid_api/models/transfer_sweep_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferSweepGetResponse](the_plaid_api/models/transfer_sweep_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_sweep_list(body: TransferSweepListRequest | TransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransferSweepListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/sweep/list` endpoint fetches sweeps matching the given filters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.transfer_sweep_list(TransferSweepListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferSweepListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.transfer_sweep_list(TransferSweepListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransferSweepListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferSweepListRequest](the_plaid_api/models/transfer_sweep_list_request.py) \| [TransferSweepListRequestDict](the_plaid_api/models/transfer_sweep_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[TransferSweepListResponse](the_plaid_api/models/transfer_sweep_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransferSweepListResponse](the_plaid_api/models/transfer_sweep_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_account_session_event_send(body: UserAccountSessionEventSendRequest | UserAccountSessionEventSendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserAccountSessionEventSendResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows sending client-specific events related to Layer sessions for analytics and tracking purposes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_account_session_event_send(
    UserAccountSessionEventSendRequest(
        link_session_id="some example string",
        event=UserAccountSessionEvent(
            name="some example string", timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserAccountSessionEventSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_account_session_event_send(
    UserAccountSessionEventSendRequest(
        link_session_id="some example string",
        event=UserAccountSessionEvent(
            name="some example string", timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserAccountSessionEventSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserAccountSessionEventSendRequest](the_plaid_api/models/user_account_session_event_send_request.py) \| [UserAccountSessionEventSendRequestDict](the_plaid_api/models/user_account_session_event_send_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserAccountSessionEventSendResponse](the_plaid_api/models/user_account_session_event_send_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserAccountSessionEventSendResponse](the_plaid_api/models/user_account_session_event_send_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_account_session_get(body: UserAccountSessionGetRequest | UserAccountSessionGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserAccountSessionGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns user permissioned account data, including identity and Item access tokens, for use with [Plaid Layer](https://plaid.com/docs/layer). Note that end users are permitted to edit the prefilled identity data in the Link flow before sharing it with you; you should treat any identity data returned by this endpoint as user-submitted, unverified data. For a verification layer, you can add [Identity Verification](https://plaid.com/docs/identity-verification/) to your flow, or check the submitted identity data against bank account data from linked accounts using [Identity Match](https://plaid.com/docs/identity/#identity-match).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_account_session_get(
    UserAccountSessionGetRequest(public_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserAccountSessionGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_account_session_get(
    UserAccountSessionGetRequest(public_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserAccountSessionGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserAccountSessionGetRequest](the_plaid_api/models/user_account_session_get_request.py) \| [UserAccountSessionGetRequestDict](the_plaid_api/models/user_account_session_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserAccountSessionGetResponse](the_plaid_api/models/user_account_session_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserAccountSessionGetResponse](the_plaid_api/models/user_account_session_get_response.py)</code> -- success

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_create(body: UserCreateRequest | UserCreateRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

For Plaid products and flows that use the user object, `/user/create` provides you a single token to access all data associated with the user. You must call this endpoint before calling `/link/token/create` if you are using any of the following: Plaid Check, Income Verification, Multi-Item Link, or Plaid Protect (Identity). If you are using Plaid Protect Link session scoring, you do not need to call `/user/create` first; Plaid will resolve or create the user when `user.client_user_id` is provided in `/link/token/create`.
For customers who began using this endpoint on or after December 10, 2025, this endpoint takes a `client_user_id` and an `identity` object and will return a `user_id`. For customers who began using it before that date, the endpoint takes a `client_user_id` and a `consumer_report_user_identity` object and will return a `user_token` and `user_id`. For more details, see [New User APIs](https://plaid.com/docs/api/users/user-apis).
In order to create a Plaid Check Consumer Report for a user, the `identity` (new) or `consumer_report_user_identity` (legacy) object must be present. If it is not provided during the `/user/create` call, it can be added later by calling `/user/update`.

In order to generate a Plaid Check Consumer Report, the following `identity` fields, at minimum, are required and must be non-empty: `name`, `date_of_birth`, `emails`, `phone_numbers`, and `addresses` (with at least one email, phone number, and address designated as `primary`). Plaid Check Consumer Reports can only be created for US-based users; the user's address country must be `US`. If creating a report for sharing with a GSE such as Fannie or Freddie, the user's full SSN must be provided via the `id_numbers` field. Providing at least a partial SSN is also strongly recommended for all use cases, since it improves the accuracy of matching user records during compliance processes such as file disclosure, dispute, or security freeze requests.


When using Plaid Protect, it is highly recommended that you provide an `identity` object to better identify and block fraud across your Link sessions.


Plaid will normalize identity fields before storing them and utilize the same identity across different user-based products.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_create(UserCreateRequest(client_user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_create(UserCreateRequest(client_user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserCreateRequest](the_plaid_api/models/user_create_request.py) \| [UserCreateRequestDict](the_plaid_api/models/user_create_request.py)</code> | The request body. |
| <code>plaid_new_user_api_enabled</code> | <code>bool \| None</code> | The HTTP header used in API requests to determine which set of User APIs to invoke: the legacy CRA version or the new User API version.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserCreateResponse](the_plaid_api/models/user_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserCreateResponse](the_plaid_api/models/user_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_financial_data_refresh(body: UserFinancialDataRefreshRequest | UserFinancialDataRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserFinancialDataRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/user/financial_data/refresh` is an optional endpoint that initiates an on-demand extraction to fetch the newest transactions for a User using the Financial Insights bundle.
This bundle refreshes the Transactions, Investments, and Liabilities product data.
This endpoint is for clients who use the Financial Insights bundle and want to proactively update all linked Items under a user.
The refresh may succeed or fail on a per-Item basis. Use the `results` array in the response to understand the outcome for each Item.

This endpoint is distinct from `/transactions/refresh`, which triggers a refresh for a single Item. Use `/user/financial_data/refresh` to target all Items for a user instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_financial_data_refresh(
    UserFinancialDataRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserFinancialDataRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_financial_data_refresh(
    UserFinancialDataRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserFinancialDataRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserFinancialDataRefreshRequest](the_plaid_api/models/user_financial_data_refresh_request.py) \| [UserFinancialDataRefreshRequestDict](the_plaid_api/models/user_financial_data_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserFinancialDataRefreshResponse](the_plaid_api/models/user_financial_data_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserFinancialDataRefreshResponse](the_plaid_api/models/user_financial_data_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_get(body: UserGetRequest | UserGetRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get user details using a `user_id`. This endpoint only supports users that were created on the new user API flow, without a `user_token`. For more details, see [New User APIs](https://plaid.com/docs/api/users/user-apis).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_get(UserGetRequest(user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_get(UserGetRequest(user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserGetRequest](the_plaid_api/models/user_get_request.py) \| [UserGetRequestDict](the_plaid_api/models/user_get_request.py)</code> | The request body. |
| <code>plaid_new_user_api_enabled</code> | <code>bool \| None</code> | The HTTP header used in API requests to determine which set of User APIs to invoke: the legacy CRA version or the new User API version.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserGetResponse](the_plaid_api/models/user_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserGetResponse](the_plaid_api/models/user_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_identity_remove(body: UserIdentityRemoveRequest | UserIdentityRemoveRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserIdentityRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows customers to explicitly purge identity/PII data provided to Plaid for a given user. This is not exposed to customers by default, as it is meant for special scenarios or requests, but Plaid is obligated to enable customers to delete PII provided to us.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_identity_remove(UserIdentityRemoveRequest(user_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserIdentityRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_identity_remove(
    UserIdentityRemoveRequest(user_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserIdentityRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserIdentityRemoveRequest](the_plaid_api/models/user_identity_remove_request.py) \| [UserIdentityRemoveRequestDict](the_plaid_api/models/user_identity_remove_request.py)</code> | The request body. |
| <code>plaid_new_user_api_enabled</code> | <code>bool \| None</code> | The HTTP header used in API requests to determine which set of User APIs to invoke: the legacy CRA version or the new User API version.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserIdentityRemoveResponse](the_plaid_api/models/user_identity_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserIdentityRemoveResponse](the_plaid_api/models/user_identity_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_items_associate(body: UserItemsAssociateRequest | UserItemsAssociateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserItemsAssociateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Associates Items to the target user. If an Item is already associated to another user, the Item will be disassociated with the existing user and associated to the target user. This operation supports a max of 100 Items.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_items_associate(
    UserItemsAssociateRequest(user_id="some example string", item_ids=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserItemsAssociateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_items_associate(
    UserItemsAssociateRequest(user_id="some example string", item_ids=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserItemsAssociateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserItemsAssociateRequest](the_plaid_api/models/user_items_associate_request.py) \| [UserItemsAssociateRequestDict](the_plaid_api/models/user_items_associate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserItemsAssociateResponse](the_plaid_api/models/user_items_associate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserItemsAssociateResponse](the_plaid_api/models/user_items_associate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_items_get(body: UserItemsGetRequest | UserItemsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserItemsGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns Items associated with a `user_id`, along with their corresponding statuses. Plaid associates an Item with a User when it has been successfully connected within a Link session initialized with that `user_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_items_get(UserItemsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserItemsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_items_get(UserItemsGetRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserItemsGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserItemsGetRequest](the_plaid_api/models/user_items_get_request.py) \| [UserItemsGetRequestDict](the_plaid_api/models/user_items_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserItemsGetResponse](the_plaid_api/models/user_items_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserItemsGetResponse](the_plaid_api/models/user_items_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_items_remove(body: UserItemsRemoveRequest | UserItemsRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserItemsRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes specific Items associated with a user. It is equivalent to calling `/item/remove` on each Item individually, but supports use cases (such as Plaid Check) where access tokens are not available. All specified Items must belong to the user or the entire operation fails. Similar to `/item/remove`, this deletes Item product data and terminates billing on the Item's products. Once removed, Items cannot be reconnected without going through Link again.
This endpoint is not intended to remove all data for a user, as it will only remove Items and no other data for the user. If the user has any user-based recurring subscription products (Financial Management, Plaid Protect, or CRA Cash Flow Updates) and is deleting their account with your product, also call `/user/products/terminate` to end those subscriptions; per-Item billing is already terminated by this endpoint. For a user initiated data deletion request, see the [Consumer Service Center](https://plaid.com/check/consumer-service-center/) to revoke access to data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_items_remove(UserItemsRemoveRequest(item_ids=["some example string"]))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserItemsRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_items_remove(
    UserItemsRemoveRequest(item_ids=["some example string"])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserItemsRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserItemsRemoveRequest](the_plaid_api/models/user_items_remove_request.py) \| [UserItemsRemoveRequestDict](the_plaid_api/models/user_items_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserItemsRemoveResponse](the_plaid_api/models/user_items_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserItemsRemoveResponse](the_plaid_api/models/user_items_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_products_terminate(body: UserProductsTerminateRequest | UserProductsTerminateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserProductsTerminateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Terminates user-based recurring subscription bundles or products (Financial Management, Plaid Protect, and CRA Cash Flow Updates) associated with a `user_id`. After you call this endpoint, the user will no longer be billed for these products. For CRA Monitoring, the subscription is canceled but historical data remains available for future report requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_products_terminate(
    UserProductsTerminateRequest(
        user_id="usr_8c3ZbDBYjaqUXZ",
        reason_code=ProductsTerminateReasonCode.CONSUMER_ACCOUNT_CLOSED,
        reason_note="User closed account with client.",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserProductsTerminateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_products_terminate(
    UserProductsTerminateRequest(
        user_id="usr_8c3ZbDBYjaqUXZ",
        reason_code=ProductsTerminateReasonCode.CONSUMER_ACCOUNT_CLOSED,
        reason_note="User closed account with client.",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserProductsTerminateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserProductsTerminateRequest](the_plaid_api/models/user_products_terminate_request.py) \| [UserProductsTerminateRequestDict](the_plaid_api/models/user_products_terminate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserProductsTerminateResponse](the_plaid_api/models/user_products_terminate_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserProductsTerminateResponse](the_plaid_api/models/user_products_terminate_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_remove(body: UserRemoveRequest | UserRemoveRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/user/remove` deletes a `user_id` or `user_token` and associated information, including any Items associated with the user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_remove(UserRemoveRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_remove(UserRemoveRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserRemoveRequest](the_plaid_api/models/user_remove_request.py) \| [UserRemoveRequestDict](the_plaid_api/models/user_remove_request.py)</code> | The request body. |
| <code>plaid_new_user_api_enabled</code> | <code>bool \| None</code> | The HTTP header used in API requests to determine which set of User APIs to invoke: the legacy CRA version or the new User API version.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserRemoveResponse](the_plaid_api/models/user_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserRemoveResponse](the_plaid_api/models/user_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_third_party_token_create(body: UserThirdPartyTokenCreateRequest | UserThirdPartyTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserThirdPartyTokenCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint is used to create a third-party user token. This token can be shared with and used by a specified third-party client to access data associated with the user through supported endpoints.

Ensure you store the `third_party_user_token` along with the `user_token` and `third_party_client_id`, as it is not possible to retrieve a previously created `third_party_user_token`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_third_party_token_create(
    UserThirdPartyTokenCreateRequest(third_party_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserThirdPartyTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_third_party_token_create(
    UserThirdPartyTokenCreateRequest(third_party_client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserThirdPartyTokenCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserThirdPartyTokenCreateRequest](the_plaid_api/models/user_third_party_token_create_request.py) \| [UserThirdPartyTokenCreateRequestDict](the_plaid_api/models/user_third_party_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserThirdPartyTokenCreateResponse](the_plaid_api/models/user_third_party_token_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserThirdPartyTokenCreateResponse](the_plaid_api/models/user_third_party_token_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_third_party_token_remove(body: UserThirdPartyTokenRemoveRequest | UserThirdPartyTokenRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserThirdPartyTokenRemoveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint is used to delete a third-party user token. Once removed, the token can no longer be used to access data associated with the user.

Any subsequent calls to retrieve information using the same third-party user token will result in an error stating the third-party user token does not exist.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_third_party_token_remove(
    UserThirdPartyTokenRemoveRequest(third_party_user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserThirdPartyTokenRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_third_party_token_remove(
    UserThirdPartyTokenRemoveRequest(third_party_user_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserThirdPartyTokenRemoveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserThirdPartyTokenRemoveRequest](the_plaid_api/models/user_third_party_token_remove_request.py) \| [UserThirdPartyTokenRemoveRequestDict](the_plaid_api/models/user_third_party_token_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserThirdPartyTokenRemoveResponse](the_plaid_api/models/user_third_party_token_remove_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserThirdPartyTokenRemoveResponse](the_plaid_api/models/user_third_party_token_remove_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_transactions_refresh(body: UserTransactionsRefreshRequest | UserTransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserTransactionsRefreshResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/user/transactions/refresh` is an optional endpoint that initiates an on-demand extraction to fetch the newest transactions for a User using the Transactions bundle.
This bundle refreshes only the Transactions product data.
This endpoint is for clients who use the Transactions Insights bundle and want to proactively update all linked Items under a user.
The refresh may succeed or fail on a per-Item basis. Use the `results` array in the response to understand the outcome for each Item.

This endpoint is distinct from `/transactions/refresh`, which triggers a refresh for a single Item. Use `/user/transactions/refresh` to target all Items for a user instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_transactions_refresh(
    UserTransactionsRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserTransactionsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_transactions_refresh(
    UserTransactionsRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserTransactionsRefreshResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserTransactionsRefreshRequest](the_plaid_api/models/user_transactions_refresh_request.py) \| [UserTransactionsRefreshRequestDict](the_plaid_api/models/user_transactions_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserTransactionsRefreshResponse](the_plaid_api/models/user_transactions_refresh_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserTransactionsRefreshResponse](the_plaid_api/models/user_transactions_refresh_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_update(body: UserUpdateRequest | UserUpdateRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint updates user information for an existing `user_id` or `user_token`. If an existing `user_id` or `user_token` is missing fields required for a given use case (e.g. creating a Consumer Report) use `/user/update` to add values for those fields.

Identity updates use merge semantics: provided fields overwrite existing ones; omitted fields remain unchanged.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.user_update(UserUpdateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.user_update(UserUpdateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UserUpdateRequest](the_plaid_api/models/user_update_request.py) \| [UserUpdateRequestDict](the_plaid_api/models/user_update_request.py)</code> | The request body. |
| <code>plaid_new_user_api_enabled</code> | <code>bool \| None</code> | The HTTP header used in API requests to determine which set of User APIs to invoke: the legacy CRA version or the new User API version.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[UserUpdateResponse](the_plaid_api/models/user_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserUpdateResponse](the_plaid_api/models/user_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_create(body: WalletCreateRequest | WalletCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WalletCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create an e-wallet. The response is the newly created e-wallet object.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.wallet_create(WalletCreateRequest(iso_currency_code=IsoCurrencyCode.GBP))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.wallet_create(WalletCreateRequest(iso_currency_code=IsoCurrencyCode.GBP))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WalletCreateRequest](the_plaid_api/models/wallet_create_request.py) \| [WalletCreateRequestDict](the_plaid_api/models/wallet_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WalletCreateResponse](the_plaid_api/models/wallet_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WalletCreateResponse](the_plaid_api/models/wallet_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_get(body: WalletGetRequest | WalletGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WalletGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch an e-wallet. The response includes the current balance.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.wallet_get(WalletGetRequest(wallet_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.wallet_get(WalletGetRequest(wallet_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WalletGetRequest](the_plaid_api/models/wallet_get_request.py) \| [WalletGetRequestDict](the_plaid_api/models/wallet_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WalletGetResponse](the_plaid_api/models/wallet_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WalletGetResponse](the_plaid_api/models/wallet_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_list(body: WalletListRequest | WalletListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WalletListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists all e-wallets in descending order of creation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.wallet_list(WalletListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.wallet_list(WalletListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WalletListRequest](the_plaid_api/models/wallet_list_request.py) \| [WalletListRequestDict](the_plaid_api/models/wallet_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WalletListResponse](the_plaid_api/models/wallet_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WalletListResponse](the_plaid_api/models/wallet_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_transaction_execute(body: WalletTransactionExecuteRequest | WalletTransactionExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WalletTransactionExecuteResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Execute a transaction using the specified e-wallet.
Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate transactions, the amount and reference for the transaction.
Transactions will settle in seconds to several days, depending on the underlying payment rail.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.wallet_transaction_execute(
    WalletTransactionExecuteRequest(
        idempotency_key="some example string",
        wallet_id="some example string",
        counterparty=WalletTransactionCounterparty(
            name="some example string", numbers=WalletTransactionCounterpartyNumbers()
        ),
        amount=WalletTransactionAmount(iso_currency_code=IsoCurrencyCode.GBP, value=1.5),
        reference="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletTransactionExecuteResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.wallet_transaction_execute(
    WalletTransactionExecuteRequest(
        idempotency_key="some example string",
        wallet_id="some example string",
        counterparty=WalletTransactionCounterparty(
            name="some example string", numbers=WalletTransactionCounterpartyNumbers()
        ),
        amount=WalletTransactionAmount(iso_currency_code=IsoCurrencyCode.GBP, value=1.5),
        reference="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletTransactionExecuteResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WalletTransactionExecuteRequest](the_plaid_api/models/wallet_transaction_execute_request.py) \| [WalletTransactionExecuteRequestDict](the_plaid_api/models/wallet_transaction_execute_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WalletTransactionExecuteResponse](the_plaid_api/models/wallet_transaction_execute_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WalletTransactionExecuteResponse](the_plaid_api/models/wallet_transaction_execute_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_transaction_get(body: WalletTransactionGetRequest | WalletTransactionGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WalletTransactionGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch a specific e-wallet transaction

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.wallet_transaction_get(
    WalletTransactionGetRequest(transaction_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletTransactionGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.wallet_transaction_get(
    WalletTransactionGetRequest(transaction_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletTransactionGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WalletTransactionGetRequest](the_plaid_api/models/wallet_transaction_get_request.py) \| [WalletTransactionGetRequestDict](the_plaid_api/models/wallet_transaction_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WalletTransactionGetResponse](the_plaid_api/models/wallet_transaction_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WalletTransactionGetResponse](the_plaid_api/models/wallet_transaction_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_transaction_list(body: WalletTransactionListRequest | WalletTransactionListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WalletTransactionListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the `created_at` time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.wallet_transaction_list(WalletTransactionListRequest(wallet_id="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletTransactionListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.wallet_transaction_list(
    WalletTransactionListRequest(wallet_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WalletTransactionListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WalletTransactionListRequest](the_plaid_api/models/wallet_transaction_list_request.py) \| [WalletTransactionListRequestDict](the_plaid_api/models/wallet_transaction_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WalletTransactionListResponse](the_plaid_api/models/wallet_transaction_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WalletTransactionListResponse](the_plaid_api/models/wallet_transaction_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_create(body: WatchlistScreeningEntityCreateRequest | WatchlistScreeningEntityCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_create(
    WatchlistScreeningEntityCreateRequest(
        search_terms=EntityWatchlistSearchTerms(
            entity_watchlist_program_id="some example string", legal_name="some example string"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_create(
    WatchlistScreeningEntityCreateRequest(
        search_terms=EntityWatchlistSearchTerms(
            entity_watchlist_program_id="some example string", legal_name="some example string"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityCreateRequest](the_plaid_api/models/watchlist_screening_entity_create_request.py) \| [WatchlistScreeningEntityCreateRequestDict](the_plaid_api/models/watchlist_screening_entity_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityCreateResponse](the_plaid_api/models/watchlist_screening_entity_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityCreateResponse](the_plaid_api/models/watchlist_screening_entity_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_get(body: WatchlistScreeningEntityGetRequest | WatchlistScreeningEntityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve an entity watchlist screening.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_get(
    WatchlistScreeningEntityGetRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_get(
    WatchlistScreeningEntityGetRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityGetRequest](the_plaid_api/models/watchlist_screening_entity_get_request.py) \| [WatchlistScreeningEntityGetRequestDict](the_plaid_api/models/watchlist_screening_entity_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityGetResponse](the_plaid_api/models/watchlist_screening_entity_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityGetResponse](the_plaid_api/models/watchlist_screening_entity_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_history_list(body: WatchlistScreeningEntityHistoryListRequest | WatchlistScreeningEntityHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityHistoryListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_history_list(
    WatchlistScreeningEntityHistoryListRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityHistoryListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_history_list(
    WatchlistScreeningEntityHistoryListRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityHistoryListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityHistoryListRequest](the_plaid_api/models/watchlist_screening_entity_history_list_request.py) \| [WatchlistScreeningEntityHistoryListRequestDict](the_plaid_api/models/watchlist_screening_entity_history_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityHistoryListResponse](the_plaid_api/models/watchlist_screening_entity_history_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityHistoryListResponse](the_plaid_api/models/watchlist_screening_entity_history_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_hit_list(body: WatchlistScreeningEntityHitListRequest | WatchlistScreeningEntityHitListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityHitListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all hits for the entity watchlist screening.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_hit_list(
    WatchlistScreeningEntityHitListRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityHitListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_hit_list(
    WatchlistScreeningEntityHitListRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityHitListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityHitListRequest](the_plaid_api/models/watchlist_screening_entity_hit_list_request.py) \| [WatchlistScreeningEntityHitListRequestDict](the_plaid_api/models/watchlist_screening_entity_hit_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityHitListResponse](the_plaid_api/models/watchlist_screening_entity_hit_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityHitListResponse](the_plaid_api/models/watchlist_screening_entity_hit_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_list(body: WatchlistScreeningEntityListRequest | WatchlistScreeningEntityListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all entity screenings.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_list(
    WatchlistScreeningEntityListRequest(entity_watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_list(
    WatchlistScreeningEntityListRequest(entity_watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityListRequest](the_plaid_api/models/watchlist_screening_entity_list_request.py) \| [WatchlistScreeningEntityListRequestDict](the_plaid_api/models/watchlist_screening_entity_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityListResponse](the_plaid_api/models/watchlist_screening_entity_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityListResponse](the_plaid_api/models/watchlist_screening_entity_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_program_get(body: WatchlistScreeningEntityProgramGetRequest | WatchlistScreeningEntityProgramGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityProgramGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get an entity watchlist screening program

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_program_get(
    WatchlistScreeningEntityProgramGetRequest(entity_watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityProgramGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_program_get(
    WatchlistScreeningEntityProgramGetRequest(entity_watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityProgramGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityProgramGetRequest](the_plaid_api/models/watchlist_screening_entity_program_get_request.py) \| [WatchlistScreeningEntityProgramGetRequestDict](the_plaid_api/models/watchlist_screening_entity_program_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityProgramGetResponse](the_plaid_api/models/watchlist_screening_entity_program_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityProgramGetResponse](the_plaid_api/models/watchlist_screening_entity_program_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_program_list(body: WatchlistScreeningEntityProgramListRequest | WatchlistScreeningEntityProgramListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityProgramListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all entity watchlist screening programs

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_program_list(WatchlistScreeningEntityProgramListRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityProgramListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_program_list(
    WatchlistScreeningEntityProgramListRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityProgramListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityProgramListRequest](the_plaid_api/models/watchlist_screening_entity_program_list_request.py) \| [WatchlistScreeningEntityProgramListRequestDict](the_plaid_api/models/watchlist_screening_entity_program_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityProgramListResponse](the_plaid_api/models/watchlist_screening_entity_program_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityProgramListResponse](the_plaid_api/models/watchlist_screening_entity_program_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_review_create(body: WatchlistScreeningEntityReviewCreateRequest | WatchlistScreeningEntityReviewCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityReviewCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_review_create(
    WatchlistScreeningEntityReviewCreateRequest(
        confirmed_hits=["some example string"],
        dismissed_hits=["some example string"],
        entity_watchlist_screening_id="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityReviewCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_review_create(
    WatchlistScreeningEntityReviewCreateRequest(
        confirmed_hits=["some example string"],
        dismissed_hits=["some example string"],
        entity_watchlist_screening_id="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityReviewCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityReviewCreateRequest](the_plaid_api/models/watchlist_screening_entity_review_create_request.py) \| [WatchlistScreeningEntityReviewCreateRequestDict](the_plaid_api/models/watchlist_screening_entity_review_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityReviewCreateResponse](the_plaid_api/models/watchlist_screening_entity_review_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityReviewCreateResponse](the_plaid_api/models/watchlist_screening_entity_review_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_review_list(body: WatchlistScreeningEntityReviewListRequest | WatchlistScreeningEntityReviewListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityReviewListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_review_list(
    WatchlistScreeningEntityReviewListRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityReviewListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_review_list(
    WatchlistScreeningEntityReviewListRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityReviewListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityReviewListRequest](the_plaid_api/models/watchlist_screening_entity_review_list_request.py) \| [WatchlistScreeningEntityReviewListRequestDict](the_plaid_api/models/watchlist_screening_entity_review_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityReviewListResponse](the_plaid_api/models/watchlist_screening_entity_review_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityReviewListResponse](the_plaid_api/models/watchlist_screening_entity_review_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_update(body: WatchlistScreeningEntityUpdateRequest | WatchlistScreeningEntityUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningEntityUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update an entity watchlist screening.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_entity_update(
    WatchlistScreeningEntityUpdateRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_entity_update(
    WatchlistScreeningEntityUpdateRequest(entity_watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningEntityUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningEntityUpdateRequest](the_plaid_api/models/watchlist_screening_entity_update_request.py) \| [WatchlistScreeningEntityUpdateRequestDict](the_plaid_api/models/watchlist_screening_entity_update_request.py)</code> | The entity screening was successfully updated. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningEntityUpdateResponse](the_plaid_api/models/watchlist_screening_entity_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningEntityUpdateResponse](the_plaid_api/models/watchlist_screening_entity_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_create(body: WatchlistScreeningIndividualCreateRequest | WatchlistScreeningIndividualCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_create(
    WatchlistScreeningIndividualCreateRequest(
        search_terms=WatchlistScreeningRequestSearchTerms(
            watchlist_program_id="some example string", legal_name="some example string"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_create(
    WatchlistScreeningIndividualCreateRequest(
        search_terms=WatchlistScreeningRequestSearchTerms(
            watchlist_program_id="some example string", legal_name="some example string"
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualCreateRequest](the_plaid_api/models/watchlist_screening_individual_create_request.py) \| [WatchlistScreeningIndividualCreateRequestDict](the_plaid_api/models/watchlist_screening_individual_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualCreateResponse](the_plaid_api/models/watchlist_screening_individual_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualCreateResponse](the_plaid_api/models/watchlist_screening_individual_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_get(body: WatchlistScreeningIndividualGetRequest | WatchlistScreeningIndividualGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a previously created individual watchlist screening

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_get(
    WatchlistScreeningIndividualGetRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_get(
    WatchlistScreeningIndividualGetRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualGetRequest](the_plaid_api/models/watchlist_screening_individual_get_request.py) \| [WatchlistScreeningIndividualGetRequestDict](the_plaid_api/models/watchlist_screening_individual_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualGetResponse](the_plaid_api/models/watchlist_screening_individual_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualGetResponse](the_plaid_api/models/watchlist_screening_individual_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_history_list(body: WatchlistScreeningIndividualHistoryListRequest | WatchlistScreeningIndividualHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualHistoryListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_history_list(
    WatchlistScreeningIndividualHistoryListRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualHistoryListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_history_list(
    WatchlistScreeningIndividualHistoryListRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualHistoryListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualHistoryListRequest](the_plaid_api/models/watchlist_screening_individual_history_list_request.py) \| [WatchlistScreeningIndividualHistoryListRequestDict](the_plaid_api/models/watchlist_screening_individual_history_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualHistoryListResponse](the_plaid_api/models/watchlist_screening_individual_history_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualHistoryListResponse](the_plaid_api/models/watchlist_screening_individual_history_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_hit_list(body: WatchlistScreeningIndividualHitListRequest | WatchlistScreeningIndividualHitListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualHitListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all hits found by Plaid for a particular individual watchlist screening.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_hit_list(
    WatchlistScreeningIndividualHitListRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualHitListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_hit_list(
    WatchlistScreeningIndividualHitListRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualHitListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualHitListRequest](the_plaid_api/models/watchlist_screening_individual_hit_list_request.py) \| [WatchlistScreeningIndividualHitListRequestDict](the_plaid_api/models/watchlist_screening_individual_hit_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualHitListResponse](the_plaid_api/models/watchlist_screening_individual_hit_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualHitListResponse](the_plaid_api/models/watchlist_screening_individual_hit_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_list(body: WatchlistScreeningIndividualListRequest | WatchlistScreeningIndividualListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List previously created watchlist screenings for individuals

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_list(
    WatchlistScreeningIndividualListRequest(watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_list(
    WatchlistScreeningIndividualListRequest(watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualListRequest](the_plaid_api/models/watchlist_screening_individual_list_request.py) \| [WatchlistScreeningIndividualListRequestDict](the_plaid_api/models/watchlist_screening_individual_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualListResponse](the_plaid_api/models/watchlist_screening_individual_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualListResponse](the_plaid_api/models/watchlist_screening_individual_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_program_get(body: WatchlistScreeningIndividualProgramGetRequest | WatchlistScreeningIndividualProgramGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualProgramGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get an individual watchlist screening program

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_program_get(
    WatchlistScreeningIndividualProgramGetRequest(watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualProgramGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_program_get(
    WatchlistScreeningIndividualProgramGetRequest(watchlist_program_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualProgramGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualProgramGetRequest](the_plaid_api/models/watchlist_screening_individual_program_get_request.py) \| [WatchlistScreeningIndividualProgramGetRequestDict](the_plaid_api/models/watchlist_screening_individual_program_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualProgramGetResponse](the_plaid_api/models/watchlist_screening_individual_program_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualProgramGetResponse](the_plaid_api/models/watchlist_screening_individual_program_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_program_list(body: WatchlistScreeningIndividualProgramListRequest | WatchlistScreeningIndividualProgramListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualProgramListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all individual watchlist screening programs

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_program_list(
    WatchlistScreeningIndividualProgramListRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualProgramListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_program_list(
    WatchlistScreeningIndividualProgramListRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualProgramListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualProgramListRequest](the_plaid_api/models/watchlist_screening_individual_program_list_request.py) \| [WatchlistScreeningIndividualProgramListRequestDict](the_plaid_api/models/watchlist_screening_individual_program_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualProgramListResponse](the_plaid_api/models/watchlist_screening_individual_program_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualProgramListResponse](the_plaid_api/models/watchlist_screening_individual_program_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_review_create(body: WatchlistScreeningIndividualReviewCreateRequest | WatchlistScreeningIndividualReviewCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualReviewCreateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_review_create(
    WatchlistScreeningIndividualReviewCreateRequest(
        confirmed_hits=["some example string"],
        dismissed_hits=["some example string"],
        watchlist_screening_id="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualReviewCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_review_create(
    WatchlistScreeningIndividualReviewCreateRequest(
        confirmed_hits=["some example string"],
        dismissed_hits=["some example string"],
        watchlist_screening_id="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualReviewCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualReviewCreateRequest](the_plaid_api/models/watchlist_screening_individual_review_create_request.py) \| [WatchlistScreeningIndividualReviewCreateRequestDict](the_plaid_api/models/watchlist_screening_individual_review_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualReviewCreateResponse](the_plaid_api/models/watchlist_screening_individual_review_create_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualReviewCreateResponse](the_plaid_api/models/watchlist_screening_individual_review_create_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_review_list(body: WatchlistScreeningIndividualReviewListRequest | WatchlistScreeningIndividualReviewListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualReviewListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all reviews for the individual watchlist screening.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_review_list(
    WatchlistScreeningIndividualReviewListRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualReviewListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_review_list(
    WatchlistScreeningIndividualReviewListRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualReviewListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualReviewListRequest](the_plaid_api/models/watchlist_screening_individual_review_list_request.py) \| [WatchlistScreeningIndividualReviewListRequestDict](the_plaid_api/models/watchlist_screening_individual_review_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualReviewListResponse](the_plaid_api/models/watchlist_screening_individual_review_list_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualReviewListResponse](the_plaid_api/models/watchlist_screening_individual_review_list_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_update(body: WatchlistScreeningIndividualUpdateRequest | WatchlistScreeningIndividualUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WatchlistScreeningIndividualUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update `search_terms` and `status` at the same time since editing `search_terms` may trigger an automatic `status` change.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.watchlist_screening_individual_update(
    WatchlistScreeningIndividualUpdateRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.watchlist_screening_individual_update(
    WatchlistScreeningIndividualUpdateRequest(watchlist_screening_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WatchlistScreeningIndividualUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WatchlistScreeningIndividualUpdateRequest](the_plaid_api/models/watchlist_screening_individual_update_request.py) \| [WatchlistScreeningIndividualUpdateRequestDict](the_plaid_api/models/watchlist_screening_individual_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WatchlistScreeningIndividualUpdateResponse](the_plaid_api/models/watchlist_screening_individual_update_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WatchlistScreeningIndividualUpdateResponse](the_plaid_api/models/watchlist_screening_individual_update_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def webhook_verification_key_get(body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WebhookVerificationKeyGetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.

The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.webhook_verification_key_get(
    WebhookVerificationKeyGetRequest(key_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WebhookVerificationKeyGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.webhook_verification_key_get(
    WebhookVerificationKeyGetRequest(key_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WebhookVerificationKeyGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WebhookVerificationKeyGetRequest](the_plaid_api/models/webhook_verification_key_get_request.py) \| [WebhookVerificationKeyGetRequestDict](the_plaid_api/models/webhook_verification_key_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_plaid_api/core/results.py)&#91;[WebhookVerificationKeyGetResponse](the_plaid_api/models/webhook_verification_key_get_response.py), [RawError](the_plaid_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WebhookVerificationKeyGetResponse](the_plaid_api/models/webhook_verification_key_get_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[RawError](the_plaid_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

