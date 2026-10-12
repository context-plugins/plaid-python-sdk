# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [ThePlaidApiClient](the_plaid_api/client.py)

<details>
<summary><code>def accounts_balance_get(body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AccountsGetResponse</code></summary>

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
try:
    response = client.accounts_balance_get(
        AccountsBalanceGetRequest(
            access_token="string",
            secret="string",
            client_id="string",
            options=AccountsBalanceGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.accounts_balance_get(
        AccountsBalanceGetRequest(
            access_token="string",
            secret="string",
            client_id="string",
            options=AccountsBalanceGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def accounts_get(body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AccountsGetResponse</code></summary>

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
try:
    response = client.accounts_get(
        AccountsGetRequest(
            client_id="string",
            secret="string",
            access_token="string",
            options=AccountsGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.accounts_get(
        AccountsGetRequest(
            client_id="string",
            secret="string",
            access_token="string",
            options=AccountsGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def application_get(body: ApplicationGetRequest | ApplicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApplicationGetResponse</code></summary>

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
try:
    response = client.application_get(
        ApplicationGetRequest(
            client_id="some example string", secret="some example string", application_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ApplicationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.application_get(
        ApplicationGetRequest(
            client_id="some example string", secret="some example string", application_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ApplicationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ApplicationGetResponse](the_plaid_api/models/application_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_create(body: AssetReportAuditCopyCreateRequest | AssetReportAuditCopyCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportAuditCopyCreateResponse</code></summary>

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
try:
    response = client.asset_report_audit_copy_create(
        AssetReportAuditCopyCreateRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_audit_copy_create(
        AssetReportAuditCopyCreateRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportAuditCopyCreateResponse](the_plaid_api/models/asset_report_audit_copy_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_get(body: AssetReportAuditCopyGetRequest | AssetReportAuditCopyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportGetResponse</code></summary>

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
try:
    response = client.asset_report_audit_copy_get(
        AssetReportAuditCopyGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_audit_copy_get(
        AssetReportAuditCopyGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_pdf_get(body: AssetReportAuditCopyPdfGetRequest | AssetReportAuditCopyPdfGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.asset_report_audit_copy_pdf_get(AssetReportAuditCopyPdfGetRequest(audit_copy_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.asset_report_audit_copy_pdf_get(
        AssetReportAuditCopyPdfGetRequest(audit_copy_token="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_remove(body: AssetReportAuditCopyRemoveRequest | AssetReportAuditCopyRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportAuditCopyRemoveResponse</code></summary>

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
try:
    response = client.asset_report_audit_copy_remove(
        AssetReportAuditCopyRemoveRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_audit_copy_remove(
        AssetReportAuditCopyRemoveRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportAuditCopyRemoveResponse](the_plaid_api/models/asset_report_audit_copy_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_create(body: AssetReportCreateRequest | AssetReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportCreateResponse</code></summary>

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
try:
    response = client.asset_report_create(AssetReportCreateRequest(days_requested=1))
    # TODO: Handle 'response' of type AssetReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_create(AssetReportCreateRequest(days_requested=1))
    # TODO: Handle 'response' of type AssetReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportCreateResponse](the_plaid_api/models/asset_report_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_filter(body: AssetReportFilterRequest | AssetReportFilterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportFilterResponse</code></summary>

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
try:
    response = client.asset_report_filter(
        AssetReportFilterRequest(
            asset_report_token="some example string", account_ids_to_exclude=["some example string"]
        ),
    )
    # TODO: Handle 'response' of type AssetReportFilterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_filter(
        AssetReportFilterRequest(
            asset_report_token="some example string", account_ids_to_exclude=["some example string"]
        ),
    )
    # TODO: Handle 'response' of type AssetReportFilterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportFilterResponse](the_plaid_api/models/asset_report_filter_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_get(body: AssetReportGetRequest | AssetReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportGetResponse</code></summary>

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
try:
    response = client.asset_report_get(AssetReportGetRequest())
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_get(AssetReportGetRequest())
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_pdf_get(body: AssetReportPdfgetRequest | AssetReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.asset_report_pdf_get(AssetReportPdfgetRequest(asset_report_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.asset_report_pdf_get(AssetReportPdfgetRequest(asset_report_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_refresh(body: AssetReportRefreshRequest | AssetReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportRefreshResponse</code></summary>

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
try:
    response = client.asset_report_refresh(AssetReportRefreshRequest(asset_report_token="some example string"))
    # TODO: Handle 'response' of type AssetReportRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_refresh(
        AssetReportRefreshRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportRefreshResponse](the_plaid_api/models/asset_report_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_remove(body: AssetReportRemoveRequest | AssetReportRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportRemoveResponse</code></summary>

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
try:
    response = client.asset_report_remove(AssetReportRemoveRequest(asset_report_token="some example string"))
    # TODO: Handle 'response' of type AssetReportRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_remove(
        AssetReportRemoveRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportRemoveResponse](the_plaid_api/models/asset_report_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def auth_get(body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AuthGetResponse</code></summary>

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
try:
    response = client.auth_get(AuthGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type AuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.auth_get(AuthGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type AuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AuthGetResponse](the_plaid_api/models/auth_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def auth_verify(body: AuthVerifyRequest | AuthVerifyRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AuthVerifyResponse</code></summary>

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
try:
    response = client.auth_verify(
        AuthVerifyRequest(
            numbers=AuthVerifyRequestNumbers(
                ach=AuthVerifyNumbersAch(account="some example string", routing="some example string")
            ),
        ),
    )
    # TODO: Handle 'response' of type AuthVerifyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.auth_verify(
        AuthVerifyRequest(
            numbers=AuthVerifyRequestNumbers(
                ach=AuthVerifyNumbersAch(account="some example string", routing="some example string")
            ),
        ),
    )
    # TODO: Handle 'response' of type AuthVerifyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AuthVerifyResponse](the_plaid_api/models/auth_verify_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_balance_get(body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferBalanceGetResponse</code></summary>

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
try:
    response = client.bank_transfer_balance_get(BankTransferBalanceGetRequest())
    # TODO: Handle 'response' of type BankTransferBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_balance_get(BankTransferBalanceGetRequest())
    # TODO: Handle 'response' of type BankTransferBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferBalanceGetResponse](the_plaid_api/models/bank_transfer_balance_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_cancel(body: BankTransferCancelRequest | BankTransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferCancelResponse</code></summary>

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
try:
    response = client.bank_transfer_cancel(BankTransferCancelRequest(bank_transfer_id="some example string"))
    # TODO: Handle 'response' of type BankTransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_cancel(
        BankTransferCancelRequest(bank_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type BankTransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferCancelResponse](the_plaid_api/models/bank_transfer_cancel_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_create(body: BankTransferCreateRequest | BankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferCreateResponse</code></summary>

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
try:
    response = client.bank_transfer_create(
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
    # TODO: Handle 'response' of type BankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_create(
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
    # TODO: Handle 'response' of type BankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferCreateResponse](the_plaid_api/models/bank_transfer_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_event_list(body: BankTransferEventListRequest | BankTransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferEventListResponse</code></summary>

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
try:
    response = client.bank_transfer_event_list(BankTransferEventListRequest())
    # TODO: Handle 'response' of type BankTransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_event_list(BankTransferEventListRequest())
    # TODO: Handle 'response' of type BankTransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferEventListResponse](the_plaid_api/models/bank_transfer_event_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_event_sync(body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferEventSyncResponse</code></summary>

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
try:
    response = client.bank_transfer_event_sync(BankTransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type BankTransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_event_sync(BankTransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type BankTransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferEventSyncResponse](the_plaid_api/models/bank_transfer_event_sync_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_get(body: BankTransferGetRequest | BankTransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferGetResponse</code></summary>

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
try:
    response = client.bank_transfer_get(BankTransferGetRequest(bank_transfer_id="some example string"))
    # TODO: Handle 'response' of type BankTransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_get(BankTransferGetRequest(bank_transfer_id="some example string"))
    # TODO: Handle 'response' of type BankTransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferGetResponse](the_plaid_api/models/bank_transfer_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_list(body: BankTransferListRequest | BankTransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferListResponse</code></summary>

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
try:
    response = client.bank_transfer_list(BankTransferListRequest())
    # TODO: Handle 'response' of type BankTransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_list(BankTransferListRequest())
    # TODO: Handle 'response' of type BankTransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferListResponse](the_plaid_api/models/bank_transfer_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_migrate_account(body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferMigrateAccountResponse</code></summary>

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
try:
    response = client.bank_transfer_migrate_account(
        BankTransferMigrateAccountRequest(
            account_number="some example string",
            routing_number="some example string",
            account_type="some example string",
        ),
    )
    # TODO: Handle 'response' of type BankTransferMigrateAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_migrate_account(
        BankTransferMigrateAccountRequest(
            account_number="some example string",
            routing_number="some example string",
            account_type="some example string",
        ),
    )
    # TODO: Handle 'response' of type BankTransferMigrateAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferMigrateAccountResponse](the_plaid_api/models/bank_transfer_migrate_account_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_sweep_get(body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferSweepGetResponse</code></summary>

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
try:
    response = client.bank_transfer_sweep_get(BankTransferSweepGetRequest(sweep_id="some example string"))
    # TODO: Handle 'response' of type BankTransferSweepGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_sweep_get(BankTransferSweepGetRequest(sweep_id="some example string"))
    # TODO: Handle 'response' of type BankTransferSweepGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferSweepGetResponse](the_plaid_api/models/bank_transfer_sweep_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_sweep_list(body: BankTransferSweepListRequest | BankTransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferSweepListResponse</code></summary>

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
try:
    response = client.bank_transfer_sweep_list(BankTransferSweepListRequest())
    # TODO: Handle 'response' of type BankTransferSweepListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_sweep_list(BankTransferSweepListRequest())
    # TODO: Handle 'response' of type BankTransferSweepListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BankTransferSweepListResponse](the_plaid_api/models/bank_transfer_sweep_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_account_risk_evaluate(body: BeaconAccountRiskEvaluateRequest | BeaconAccountRiskEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconAccountRiskEvaluateResponse</code></summary>

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
try:
    response = client.beacon_account_risk_evaluate(BeaconAccountRiskEvaluateRequest())
    # TODO: Handle 'response' of type BeaconAccountRiskEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_account_risk_evaluate(BeaconAccountRiskEvaluateRequest())
    # TODO: Handle 'response' of type BeaconAccountRiskEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconAccountRiskEvaluateResponse](the_plaid_api/models/beacon_account_risk_evaluate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_duplicate_get(body: BeaconDuplicateGetRequest | BeaconDuplicateGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconDuplicateGetResponse</code></summary>

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
try:
    response = client.beacon_duplicate_get(BeaconDuplicateGetRequest(beacon_duplicate_id="some example string"))
    # TODO: Handle 'response' of type BeaconDuplicateGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_duplicate_get(
        BeaconDuplicateGetRequest(beacon_duplicate_id="some example string")
    )
    # TODO: Handle 'response' of type BeaconDuplicateGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconDuplicateGetResponse](the_plaid_api/models/beacon_duplicate_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_create(body: BeaconReportCreateRequest | BeaconReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconReportCreateResponse</code></summary>

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
try:
    response = client.beacon_report_create(
        BeaconReportCreateRequest(
            beacon_user_id="some example string", type_=BeaconReportCreateType.FIRST_PARTY, fraud_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type BeaconReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_report_create(
        BeaconReportCreateRequest(
            beacon_user_id="some example string", type_=BeaconReportCreateType.FIRST_PARTY, fraud_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type BeaconReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconReportCreateResponse](the_plaid_api/models/beacon_report_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_get(body: BeaconReportGetRequest | BeaconReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconReportGetResponse</code></summary>

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
try:
    response = client.beacon_report_get(BeaconReportGetRequest(beacon_report_id="some example string"))
    # TODO: Handle 'response' of type BeaconReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_report_get(BeaconReportGetRequest(beacon_report_id="some example string"))
    # TODO: Handle 'response' of type BeaconReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconReportGetResponse](the_plaid_api/models/beacon_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_list(body: BeaconReportListRequest | BeaconReportListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconReportListResponse</code></summary>

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
try:
    response = client.beacon_report_list(BeaconReportListRequest(beacon_user_id="some example string"))
    # TODO: Handle 'response' of type BeaconReportListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_report_list(BeaconReportListRequest(beacon_user_id="some example string"))
    # TODO: Handle 'response' of type BeaconReportListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconReportListResponse](the_plaid_api/models/beacon_report_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_syndication_get(body: BeaconReportSyndicationGetRequest | BeaconReportSyndicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconReportSyndicationGetResponse</code></summary>

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
try:
    response = client.beacon_report_syndication_get(
        BeaconReportSyndicationGetRequest(beacon_report_syndication_id="some example string")
    )
    # TODO: Handle 'response' of type BeaconReportSyndicationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_report_syndication_get(
        BeaconReportSyndicationGetRequest(beacon_report_syndication_id="some example string")
    )
    # TODO: Handle 'response' of type BeaconReportSyndicationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconReportSyndicationGetResponse](the_plaid_api/models/beacon_report_syndication_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_report_syndication_list(body: BeaconReportSyndicationListRequest | BeaconReportSyndicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconReportSyndicationListResponse</code></summary>

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
try:
    response = client.beacon_report_syndication_list(
        BeaconReportSyndicationListRequest(beacon_user_id="some example string")
    )
    # TODO: Handle 'response' of type BeaconReportSyndicationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_report_syndication_list(
        BeaconReportSyndicationListRequest(beacon_user_id="some example string")
    )
    # TODO: Handle 'response' of type BeaconReportSyndicationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconReportSyndicationListResponse](the_plaid_api/models/beacon_report_syndication_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_account_insights_get(body: BeaconUserAccountInsightsGetRequest | BeaconUserAccountInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconUserAccountInsightsGetResponse</code></summary>

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
try:
    response = client.beacon_user_account_insights_get(
        BeaconUserAccountInsightsGetRequest(beacon_user_id="some example string", access_token="some example string")
    )
    # TODO: Handle 'response' of type BeaconUserAccountInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_user_account_insights_get(
        BeaconUserAccountInsightsGetRequest(beacon_user_id="some example string", access_token="some example string")
    )
    # TODO: Handle 'response' of type BeaconUserAccountInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconUserAccountInsightsGetResponse](the_plaid_api/models/beacon_user_account_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_create(body: BeaconUserCreateRequest | BeaconUserCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconUserCreateResponse</code></summary>

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
try:
    response = client.beacon_user_create(
        BeaconUserCreateRequest(
            program_id="some example string",
            client_user_id="some example string",
            user=BeaconUserRequestData(
                name=BeaconUserName(given_name="some example string", family_name="some example string")
            ),
        ),
    )
    # TODO: Handle 'response' of type BeaconUserCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_user_create(
        BeaconUserCreateRequest(
            program_id="some example string",
            client_user_id="some example string",
            user=BeaconUserRequestData(
                name=BeaconUserName(given_name="some example string", family_name="some example string")
            ),
        ),
    )
    # TODO: Handle 'response' of type BeaconUserCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconUserCreateResponse](the_plaid_api/models/beacon_user_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_get(body: BeaconUserGetRequest | BeaconUserGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconUserGetResponse</code></summary>

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
try:
    response = client.beacon_user_get(BeaconUserGetRequest(beacon_user_id="some example string"))
    # TODO: Handle 'response' of type BeaconUserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_user_get(BeaconUserGetRequest(beacon_user_id="some example string"))
    # TODO: Handle 'response' of type BeaconUserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconUserGetResponse](the_plaid_api/models/beacon_user_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_history_list(body: BeaconUserHistoryListRequest | BeaconUserHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconUserHistoryListResponse</code></summary>

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
try:
    response = client.beacon_user_history_list(BeaconUserHistoryListRequest(beacon_user_id="some example string"))
    # TODO: Handle 'response' of type BeaconUserHistoryListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_user_history_list(
        BeaconUserHistoryListRequest(beacon_user_id="some example string")
    )
    # TODO: Handle 'response' of type BeaconUserHistoryListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconUserHistoryListResponse](the_plaid_api/models/beacon_user_history_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_review(body: BeaconUserReviewRequest | BeaconUserReviewRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconUserGetResponse</code></summary>

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
try:
    response = client.beacon_user_review(
        BeaconUserReviewRequest(beacon_user_id="some example string", status=BeaconUserStatus.REJECTED)
    )
    # TODO: Handle 'response' of type BeaconUserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_user_review(
        BeaconUserReviewRequest(beacon_user_id="some example string", status=BeaconUserStatus.REJECTED)
    )
    # TODO: Handle 'response' of type BeaconUserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconUserGetResponse](the_plaid_api/models/beacon_user_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beacon_user_update(body: BeaconUserUpdateRequest | BeaconUserUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BeaconUserUpdateResponse</code></summary>

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
try:
    response = client.beacon_user_update(BeaconUserUpdateRequest(beacon_user_id="some example string"))
    # TODO: Handle 'response' of type BeaconUserUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beacon_user_update(BeaconUserUpdateRequest(beacon_user_id="some example string"))
    # TODO: Handle 'response' of type BeaconUserUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BeaconUserUpdateResponse](the_plaid_api/models/beacon_user_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_ewa_report_v1_get(body: BetaEwaReportV1GetRequest | BetaEwaReportV1GetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BetaEwaReportV1GetResponse</code></summary>

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
try:
    response = client.beta_ewa_report_v1_get(
        BetaEwaReportV1GetRequest(access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175")
    )
    # TODO: Handle 'response' of type BetaEwaReportV1GetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beta_ewa_report_v1_get(
        BetaEwaReportV1GetRequest(access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175")
    )
    # TODO: Handle 'response' of type BetaEwaReportV1GetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BetaEwaReportV1GetResponse](the_plaid_api/models/beta_ewa_report_v1_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_create(body: BetaPartnerCustomerV1CreateRequest | BetaPartnerCustomerV1CreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BetaPartnerCustomerV1CreateResponse</code></summary>

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
try:
    response = client.beta_partner_customer_v1_create(
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
    # TODO: Handle 'response' of type BetaPartnerCustomerV1CreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beta_partner_customer_v1_create(
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
    # TODO: Handle 'response' of type BetaPartnerCustomerV1CreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BetaPartnerCustomerV1CreateResponse](the_plaid_api/models/beta_partner_customer_v1_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_enable(body: BetaPartnerCustomerV1EnableRequest | BetaPartnerCustomerV1EnableRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BetaPartnerCustomerV1EnableResponse</code></summary>

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
try:
    response = client.beta_partner_customer_v1_enable(
        BetaPartnerCustomerV1EnableRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="634758733ebb4f00134b85ea",
            products=[Products.AUTH],
        ),
    )
    # TODO: Handle 'response' of type BetaPartnerCustomerV1EnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beta_partner_customer_v1_enable(
        BetaPartnerCustomerV1EnableRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="634758733ebb4f00134b85ea",
            products=[Products.AUTH],
        ),
    )
    # TODO: Handle 'response' of type BetaPartnerCustomerV1EnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BetaPartnerCustomerV1EnableResponse](the_plaid_api/models/beta_partner_customer_v1_enable_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_get(body: BetaPartnerCustomerV1GetRequest | BetaPartnerCustomerV1GetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BetaPartnerCustomerV1GetResponse</code></summary>

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
try:
    response = client.beta_partner_customer_v1_get(
        BetaPartnerCustomerV1GetRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="634758733ebb4f00134b85ea",
        ),
    )
    # TODO: Handle 'response' of type BetaPartnerCustomerV1GetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beta_partner_customer_v1_get(
        BetaPartnerCustomerV1GetRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="634758733ebb4f00134b85ea",
        ),
    )
    # TODO: Handle 'response' of type BetaPartnerCustomerV1GetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BetaPartnerCustomerV1GetResponse](the_plaid_api/models/beta_partner_customer_v1_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def beta_partner_customer_v1_update(body: BetaPartnerCustomerV1UpdateRequest | BetaPartnerCustomerV1UpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BetaPartnerCustomerV1UpdateResponse</code></summary>

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
try:
    response = client.beta_partner_customer_v1_update(
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
    # TODO: Handle 'response' of type BetaPartnerCustomerV1UpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.beta_partner_customer_v1_update(
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
    # TODO: Handle 'response' of type BetaPartnerCustomerV1UpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BetaPartnerCustomerV1UpdateResponse](the_plaid_api/models/beta_partner_customer_v1_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_verification_create(body: BusinessVerificationCreateRequest | BusinessVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BusinessVerificationCreateResponse</code></summary>

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
try:
    response = client.business_verification_create(
        BusinessVerificationCreateRequest(client_user_id="some example string")
    )
    # TODO: Handle 'response' of type BusinessVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.business_verification_create(
        BusinessVerificationCreateRequest(client_user_id="some example string")
    )
    # TODO: Handle 'response' of type BusinessVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BusinessVerificationCreateResponse](the_plaid_api/models/business_verification_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_verification_get(body: BusinessVerificationGetRequest | BusinessVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BusinessVerificationGetResponse</code></summary>

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
try:
    response = client.business_verification_get(
        BusinessVerificationGetRequest(business_verification_id="some example string")
    )
    # TODO: Handle 'response' of type BusinessVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.business_verification_get(
        BusinessVerificationGetRequest(business_verification_id="some example string")
    )
    # TODO: Handle 'response' of type BusinessVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[BusinessVerificationGetResponse](the_plaid_api/models/business_verification_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_get(body: CashflowReportGetRequest | CashflowReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CashflowReportGetResponse</code></summary>

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
try:
    response = client.cashflow_report_get(
        CashflowReportGetRequest(access_token="some example string", days_requested=1)
    )
    # TODO: Handle 'response' of type CashflowReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cashflow_report_get(
        CashflowReportGetRequest(access_token="some example string", days_requested=1)
    )
    # TODO: Handle 'response' of type CashflowReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CashflowReportGetResponse](the_plaid_api/models/cashflow_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_insights_get(body: CashflowReportInsightsGetRequest | CashflowReportInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CashflowReportInsightsGetResponse</code></summary>

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
try:
    response = client.cashflow_report_insights_get(CashflowReportInsightsGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type CashflowReportInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cashflow_report_insights_get(
        CashflowReportInsightsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type CashflowReportInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CashflowReportInsightsGetResponse](the_plaid_api/models/cashflow_report_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_refresh(body: CashflowReportRefreshRequest | CashflowReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CashflowReportRefreshResponse</code></summary>

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
try:
    response = client.cashflow_report_refresh(
        CashflowReportRefreshRequest(access_token="some example string", days_requested=1)
    )
    # TODO: Handle 'response' of type CashflowReportRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cashflow_report_refresh(
        CashflowReportRefreshRequest(access_token="some example string", days_requested=1)
    )
    # TODO: Handle 'response' of type CashflowReportRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CashflowReportRefreshResponse](the_plaid_api/models/cashflow_report_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cashflow_report_transactions_get(body: CashflowReportTransactionsGetRequest | CashflowReportTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CashflowReportTransactionsGetResponse</code></summary>

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
try:
    response = client.cashflow_report_transactions_get(
        CashflowReportTransactionsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type CashflowReportTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cashflow_report_transactions_get(
        CashflowReportTransactionsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type CashflowReportTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CashflowReportTransactionsGetResponse](the_plaid_api/models/cashflow_report_transactions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def categories_get(body: Any, *, request_options: RequestOptionsOrDict | None = None) -> CategoriesGetResponse</code></summary>

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
try:
    response = client.categories_get({})
    # TODO: Handle 'response' of type CategoriesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories_get({})
    # TODO: Handle 'response' of type CategoriesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CategoriesGetResponse](the_plaid_api/models/categories_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def consent_events_get(body: ConsentEventsGetRequest | ConsentEventsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ConsentEventsGetResponse</code></summary>

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
try:
    response = client.consent_events_get(ConsentEventsGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ConsentEventsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.consent_events_get(ConsentEventsGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ConsentEventsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ConsentEventsGetResponse](the_plaid_api/models/consent_events_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def consumer_report_pdf_get(body: ConsumerReportPdfgetRequest | ConsumerReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.consumer_report_pdf_get(ConsumerReportPdfgetRequest(user_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.consumer_report_pdf_get(ConsumerReportPdfgetRequest(user_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_base_report_get(body: CraCheckReportBaseReportGetRequest | CraCheckReportBaseReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportBaseReportGetResponse</code></summary>

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
try:
    response = client.cra_check_report_base_report_get(CraCheckReportBaseReportGetRequest())
    # TODO: Handle 'response' of type CraCheckReportBaseReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_base_report_get(CraCheckReportBaseReportGetRequest())
    # TODO: Handle 'response' of type CraCheckReportBaseReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportBaseReportGetResponse](the_plaid_api/models/cra_check_report_base_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_cashflow_insights_get(body: CraCheckReportCashflowInsightsGetRequest | CraCheckReportCashflowInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportCashflowInsightsGetResponse</code></summary>

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
try:
    response = client.cra_check_report_cashflow_insights_get(CraCheckReportCashflowInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportCashflowInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_cashflow_insights_get(CraCheckReportCashflowInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportCashflowInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportCashflowInsightsGetResponse](the_plaid_api/models/cra_check_report_cashflow_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_create(body: CraCheckReportCreateRequest | CraCheckReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportCreateResponse</code></summary>

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
try:
    response = client.cra_check_report_create(
        CraCheckReportCreateRequest(
            webhook="some example string",
            days_requested=1,
            consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
        ),
    )
    # TODO: Handle 'response' of type CraCheckReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_create(
        CraCheckReportCreateRequest(
            webhook="some example string",
            days_requested=1,
            consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
        ),
    )
    # TODO: Handle 'response' of type CraCheckReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportCreateResponse](the_plaid_api/models/cra_check_report_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_income_insights_get(body: CraCheckReportIncomeInsightsGetRequest | CraCheckReportIncomeInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportIncomeInsightsGetResponse</code></summary>

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
try:
    response = client.cra_check_report_income_insights_get(CraCheckReportIncomeInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportIncomeInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_income_insights_get(CraCheckReportIncomeInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportIncomeInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportIncomeInsightsGetResponse](the_plaid_api/models/cra_check_report_income_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_lend_score_get(body: CraCheckReportLendScoreGetRequest | CraCheckReportLendScoreGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportLendScoreGetResponse</code></summary>

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
try:
    response = client.cra_check_report_lend_score_get(CraCheckReportLendScoreGetRequest())
    # TODO: Handle 'response' of type CraCheckReportLendScoreGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_lend_score_get(CraCheckReportLendScoreGetRequest())
    # TODO: Handle 'response' of type CraCheckReportLendScoreGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportLendScoreGetResponse](the_plaid_api/models/cra_check_report_lend_score_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_network_insights_get(body: CraCheckReportNetworkInsightsGetRequest | CraCheckReportNetworkInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportNetworkInsightsGetResponse</code></summary>

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
try:
    response = client.cra_check_report_network_insights_get(CraCheckReportNetworkInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportNetworkInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_network_insights_get(CraCheckReportNetworkInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportNetworkInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportNetworkInsightsGetResponse](the_plaid_api/models/cra_check_report_network_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_partner_insights_get(body: CraCheckReportPartnerInsightsGetRequest | CraCheckReportPartnerInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportPartnerInsightsGetResponse</code></summary>

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
try:
    response = client.cra_check_report_partner_insights_get(CraCheckReportPartnerInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportPartnerInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_partner_insights_get(CraCheckReportPartnerInsightsGetRequest())
    # TODO: Handle 'response' of type CraCheckReportPartnerInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportPartnerInsightsGetResponse](the_plaid_api/models/cra_check_report_partner_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_pdf_get(body: CraCheckReportPdfgetRequest | CraCheckReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.cra_check_report_pdf_get(CraCheckReportPdfgetRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.cra_check_report_pdf_get(CraCheckReportPdfgetRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_verification_get(body: CraCheckReportVerificationGetRequest | CraCheckReportVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCheckReportVerificationGetResponse</code></summary>

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
try:
    response = client.cra_check_report_verification_get(
        CraCheckReportVerificationGetRequest(reports_requested=[CraCheckReportVerificationGetReportType.VOA])
    )
    # TODO: Handle 'response' of type CraCheckReportVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_check_report_verification_get(
        CraCheckReportVerificationGetRequest(reports_requested=[CraCheckReportVerificationGetReportType.VOA])
    )
    # TODO: Handle 'response' of type CraCheckReportVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCheckReportVerificationGetResponse](the_plaid_api/models/cra_check_report_verification_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_check_report_verification_pdf_get(body: CraCheckReportVerificationPdfGetRequest | CraCheckReportVerificationPdfGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.cra_check_report_verification_pdf_get(CraCheckReportVerificationPdfGetRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.cra_check_report_verification_pdf_get(CraCheckReportVerificationPdfGetRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_credit_profile_report_get(body: CraCreditProfileReportGetRequest | CraCreditProfileReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraCreditProfileReportGetResponse</code></summary>

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
try:
    response = client.cra_credit_profile_report_get(
        CraCreditProfileReportGetRequest(
            user_id="some example string",
            consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
            client_report_id="some example string",
            report_type=CraCreditProfileReportType.QUALIFY,
            inquiry_type=CraCreditProfileInquiryType.SOFT_INQUIRY,
            version=CraCreditProfileReportVersion.V1,
        ),
    )
    # TODO: Handle 'response' of type CraCreditProfileReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_credit_profile_report_get(
        CraCreditProfileReportGetRequest(
            user_id="some example string",
            consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
            client_report_id="some example string",
            report_type=CraCreditProfileReportType.QUALIFY,
            inquiry_type=CraCreditProfileInquiryType.SOFT_INQUIRY,
            version=CraCreditProfileReportVersion.V1,
        ),
    )
    # TODO: Handle 'response' of type CraCreditProfileReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraCreditProfileReportGetResponse](the_plaid_api/models/cra_credit_profile_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_applications_register(body: CraLoansApplicationsRegisterRequest | CraLoansApplicationsRegisterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraLoansApplicationsRegisterResponse</code></summary>

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
try:
    response = client.cra_loans_applications_register(
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
    # TODO: Handle 'response' of type CraLoansApplicationsRegisterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_loans_applications_register(
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
    # TODO: Handle 'response' of type CraLoansApplicationsRegisterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraLoansApplicationsRegisterResponse](the_plaid_api/models/cra_loans_applications_register_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_register(body: CraloansRegisterRequest | CraloansRegisterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraLoansRegisterResponse</code></summary>

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
try:
    response = client.cra_loans_register(
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
    # TODO: Handle 'response' of type CraLoansRegisterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_loans_register(
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
    # TODO: Handle 'response' of type CraLoansRegisterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraLoansRegisterResponse](the_plaid_api/models/cra_loans_register_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_unregister(body: CraLoansUnregisterRequest | CraLoansUnregisterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraLoanUnregisterResponse</code></summary>

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
try:
    response = client.cra_loans_unregister(
        CraLoansUnregisterRequest(
            loans=[
                CraLoanUnregister(
                    loan_id="some example string",
                    closed_with_status=CraLoanClosedStatus(status=CraLoanStatus.APPROVED, date=date(2024, 1, 15)),
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CraLoanUnregisterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_loans_unregister(
        CraLoansUnregisterRequest(
            loans=[
                CraLoanUnregister(
                    loan_id="some example string",
                    closed_with_status=CraLoanClosedStatus(status=CraLoanStatus.APPROVED, date=date(2024, 1, 15)),
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CraLoanUnregisterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraLoanUnregisterResponse](the_plaid_api/models/cra_loan_unregister_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_loans_update(body: CraLoansUpdateRequest | CraLoansUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraLoansUpdateResponse</code></summary>

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
try:
    response = client.cra_loans_update(CraLoansUpdateRequest(loans=[CraLoanUpdate()]))
    # TODO: Handle 'response' of type CraLoansUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_loans_update(CraLoansUpdateRequest(loans=[CraLoanUpdate()]))
    # TODO: Handle 'response' of type CraLoansUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraLoansUpdateResponse](the_plaid_api/models/cra_loans_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_monitoring_insights_get(body: CraMonitoringInsightsGetRequest | CraMonitoringInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraMonitoringInsightsGetResponse</code></summary>

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
try:
    response = client.cra_monitoring_insights_get(
        CraMonitoringInsightsGetRequest(
            consumer_report_permissible_purpose=MonitoringConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT
        ),
    )
    # TODO: Handle 'response' of type CraMonitoringInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_monitoring_insights_get(
        CraMonitoringInsightsGetRequest(
            consumer_report_permissible_purpose=MonitoringConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT
        ),
    )
    # TODO: Handle 'response' of type CraMonitoringInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraMonitoringInsightsGetResponse](the_plaid_api/models/cra_monitoring_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_monitoring_insights_subscribe(body: CraMonitoringInsightsSubscribeRequest | CraMonitoringInsightsSubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraMonitoringInsightsSubscribeResponse</code></summary>

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
try:
    response = client.cra_monitoring_insights_subscribe(
        CraMonitoringInsightsSubscribeRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type CraMonitoringInsightsSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_monitoring_insights_subscribe(
        CraMonitoringInsightsSubscribeRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type CraMonitoringInsightsSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraMonitoringInsightsSubscribeResponse](the_plaid_api/models/cra_monitoring_insights_subscribe_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_monitoring_insights_unsubscribe(body: CraMonitoringInsightsUnsubscribeRequest | CraMonitoringInsightsUnsubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraMonitoringInsightsUnsubscribeResponse</code></summary>

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
try:
    response = client.cra_monitoring_insights_unsubscribe(
        CraMonitoringInsightsUnsubscribeRequest(subscription_id="some example string")
    )
    # TODO: Handle 'response' of type CraMonitoringInsightsUnsubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_monitoring_insights_unsubscribe(
        CraMonitoringInsightsUnsubscribeRequest(subscription_id="some example string")
    )
    # TODO: Handle 'response' of type CraMonitoringInsightsUnsubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraMonitoringInsightsUnsubscribeResponse](the_plaid_api/models/cra_monitoring_insights_unsubscribe_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_partner_insights_get(body: CraPartnerInsightsGetRequest | CraPartnerInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraPartnerInsightsGetResponse</code></summary>

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
try:
    response = client.cra_partner_insights_get(CraPartnerInsightsGetRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CraPartnerInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_partner_insights_get(
        CraPartnerInsightsGetRequest(user_token="some example string")
    )
    # TODO: Handle 'response' of type CraPartnerInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraPartnerInsightsGetResponse](the_plaid_api/models/cra_partner_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cra_report_get(body: CraReportGetRequest | CraReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CraReportGetResponse</code></summary>

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
try:
    response = client.cra_report_get(
        CraReportGetRequest(
            user_id="some example string",
            products=[CraReportGetRequestProduct(product=Products.ASSETS, version="some example string")],
            decision_stage=CraReportDecisionStage.PREQUALIFICATION,
            consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
        ),
    )
    # TODO: Handle 'response' of type CraReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cra_report_get(
        CraReportGetRequest(
            user_id="some example string",
            products=[CraReportGetRequestProduct(product=Products.ASSETS, version="some example string")],
            decision_stage=CraReportDecisionStage.PREQUALIFICATION,
            consumer_report_permissible_purpose=ConsumerReportPermissiblePurpose.ACCOUNT_REVIEW_CREDIT,
        ),
    )
    # TODO: Handle 'response' of type CraReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CraReportGetResponse](the_plaid_api/models/cra_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_payment_token(body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentTokenCreateResponse</code></summary>

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
try:
    response = client.create_payment_token(PaymentInitiationPaymentTokenCreateRequest(payment_id="some example string"))
    # TODO: Handle 'response' of type PaymentInitiationPaymentTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.create_payment_token(
        PaymentInitiationPaymentTokenCreateRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationPaymentTokenCreateResponse](the_plaid_api/models/payment_initiation_payment_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_asset_report_freddie_mac_get(body: AssetReportFreddieGetRequest | AssetReportFreddieGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportFreddieGetResponse</code></summary>

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
try:
    response = client.credit_asset_report_freddie_mac_get(
        AssetReportFreddieGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportFreddieGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_asset_report_freddie_mac_get(
        AssetReportFreddieGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportFreddieGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportFreddieGetResponse](the_plaid_api/models/asset_report_freddie_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_audit_copy_token_create(body: CreditAuditCopyTokenCreateRequest | CreditAuditCopyTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditAuditCopyTokenCreateResponse</code></summary>

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
try:
    response = client.credit_audit_copy_token_create(
        CreditAuditCopyTokenCreateRequest(report_tokens=["some example string"])
    )
    # TODO: Handle 'response' of type CreditAuditCopyTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_audit_copy_token_create(
        CreditAuditCopyTokenCreateRequest(report_tokens=["some example string"])
    )
    # TODO: Handle 'response' of type CreditAuditCopyTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditAuditCopyTokenCreateResponse](the_plaid_api/models/credit_audit_copy_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_audit_copy_token_update(body: CreditAuditCopyTokenUpdateRequest | CreditAuditCopyTokenUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditAuditCopyTokenUpdateResponse</code></summary>

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
try:
    response = client.credit_audit_copy_token_update(
        CreditAuditCopyTokenUpdateRequest(audit_copy_token="some example string", report_tokens=["some example string"])
    )
    # TODO: Handle 'response' of type CreditAuditCopyTokenUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_audit_copy_token_update(
        CreditAuditCopyTokenUpdateRequest(audit_copy_token="some example string", report_tokens=["some example string"])
    )
    # TODO: Handle 'response' of type CreditAuditCopyTokenUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditAuditCopyTokenUpdateResponse](the_plaid_api/models/credit_audit_copy_token_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_employment_get(body: CreditBankEmploymentGetRequest | CreditBankEmploymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditBankEmploymentGetResponse</code></summary>

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
try:
    response = client.credit_bank_employment_get(CreditBankEmploymentGetRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CreditBankEmploymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_bank_employment_get(
        CreditBankEmploymentGetRequest(user_token="some example string")
    )
    # TODO: Handle 'response' of type CreditBankEmploymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditBankEmploymentGetResponse](the_plaid_api/models/credit_bank_employment_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_get(body: CreditBankIncomeGetRequest | CreditBankIncomeGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditBankIncomeGetResponse</code></summary>

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
try:
    response = client.credit_bank_income_get(CreditBankIncomeGetRequest())
    # TODO: Handle 'response' of type CreditBankIncomeGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_bank_income_get(CreditBankIncomeGetRequest())
    # TODO: Handle 'response' of type CreditBankIncomeGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditBankIncomeGetResponse](the_plaid_api/models/credit_bank_income_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_pdf_get(body: CreditBankIncomePdfgetRequest | CreditBankIncomePdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.credit_bank_income_pdf_get(CreditBankIncomePdfgetRequest(user_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.credit_bank_income_pdf_get(CreditBankIncomePdfgetRequest(user_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_refresh(body: CreditBankIncomeRefreshRequest | CreditBankIncomeRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditBankIncomeRefreshResponse</code></summary>

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
try:
    response = client.credit_bank_income_refresh(CreditBankIncomeRefreshRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CreditBankIncomeRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_bank_income_refresh(
        CreditBankIncomeRefreshRequest(user_token="some example string")
    )
    # TODO: Handle 'response' of type CreditBankIncomeRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditBankIncomeRefreshResponse](the_plaid_api/models/credit_bank_income_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_income_webhook_update(body: CreditBankIncomeWebhookUpdateRequest | CreditBankIncomeWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditBankIncomeWebhookUpdateResponse</code></summary>

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
try:
    response = client.credit_bank_income_webhook_update(
        CreditBankIncomeWebhookUpdateRequest(user_token="some example string", enable_webhooks=True)
    )
    # TODO: Handle 'response' of type CreditBankIncomeWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_bank_income_webhook_update(
        CreditBankIncomeWebhookUpdateRequest(user_token="some example string", enable_webhooks=True)
    )
    # TODO: Handle 'response' of type CreditBankIncomeWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditBankIncomeWebhookUpdateResponse](the_plaid_api/models/credit_bank_income_webhook_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_bank_statements_uploads_get(body: CreditBankStatementsUploadsGetRequest | CreditBankStatementsUploadsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditBankStatementsUploadsGetResponse</code></summary>

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
try:
    response = client.credit_bank_statements_uploads_get(
        CreditBankStatementsUploadsGetRequest(user_token="some example string")
    )
    # TODO: Handle 'response' of type CreditBankStatementsUploadsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_bank_statements_uploads_get(
        CreditBankStatementsUploadsGetRequest(user_token="some example string")
    )
    # TODO: Handle 'response' of type CreditBankStatementsUploadsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditBankStatementsUploadsGetResponse](the_plaid_api/models/credit_bank_statements_uploads_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_employment_get(body: CreditEmploymentGetRequest | CreditEmploymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditEmploymentGetResponse</code></summary>

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
try:
    response = client.credit_employment_get(CreditEmploymentGetRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CreditEmploymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_employment_get(CreditEmploymentGetRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CreditEmploymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditEmploymentGetResponse](the_plaid_api/models/credit_employment_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_freddie_mac_reports_get(body: CreditFreddieMacReportsGetRequest | CreditFreddieMacReportsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditFreddieMacReportsGetResponse</code></summary>

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
try:
    response = client.credit_freddie_mac_reports_get(
        CreditFreddieMacReportsGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type CreditFreddieMacReportsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_freddie_mac_reports_get(
        CreditFreddieMacReportsGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type CreditFreddieMacReportsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditFreddieMacReportsGetResponse](the_plaid_api/models/credit_freddie_mac_reports_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_get(body: CreditPayrollIncomeGetRequest | CreditPayrollIncomeGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditPayrollIncomeGetResponse</code></summary>

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
try:
    response = client.credit_payroll_income_get(CreditPayrollIncomeGetRequest())
    # TODO: Handle 'response' of type CreditPayrollIncomeGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_payroll_income_get(CreditPayrollIncomeGetRequest())
    # TODO: Handle 'response' of type CreditPayrollIncomeGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditPayrollIncomeGetResponse](the_plaid_api/models/credit_payroll_income_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_parsing_config_update(body: CreditPayrollIncomeParsingConfigUpdateRequest | CreditPayrollIncomeParsingConfigUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditPayrollIncomeParsingConfigUpdateResponse</code></summary>

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
try:
    response = client.credit_payroll_income_parsing_config_update(
        CreditPayrollIncomeParsingConfigUpdateRequest(
            user_token="some example string", parsing_config=[IncomeVerificationDocParsingConfig.OCR]
        ),
    )
    # TODO: Handle 'response' of type CreditPayrollIncomeParsingConfigUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_payroll_income_parsing_config_update(
        CreditPayrollIncomeParsingConfigUpdateRequest(
            user_token="some example string", parsing_config=[IncomeVerificationDocParsingConfig.OCR]
        ),
    )
    # TODO: Handle 'response' of type CreditPayrollIncomeParsingConfigUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditPayrollIncomeParsingConfigUpdateResponse](the_plaid_api/models/credit_payroll_income_parsing_config_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_precheck(body: CreditPayrollIncomePrecheckRequest | CreditPayrollIncomePrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditPayrollIncomePrecheckResponse</code></summary>

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
try:
    response = client.credit_payroll_income_precheck(CreditPayrollIncomePrecheckRequest())
    # TODO: Handle 'response' of type CreditPayrollIncomePrecheckResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_payroll_income_precheck(CreditPayrollIncomePrecheckRequest())
    # TODO: Handle 'response' of type CreditPayrollIncomePrecheckResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditPayrollIncomePrecheckResponse](the_plaid_api/models/credit_payroll_income_precheck_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_refresh(body: CreditPayrollIncomeRefreshRequest | CreditPayrollIncomeRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditPayrollIncomeRefreshResponse</code></summary>

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
try:
    response = client.credit_payroll_income_refresh(CreditPayrollIncomeRefreshRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CreditPayrollIncomeRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_payroll_income_refresh(
        CreditPayrollIncomeRefreshRequest(user_token="some example string")
    )
    # TODO: Handle 'response' of type CreditPayrollIncomeRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditPayrollIncomeRefreshResponse](the_plaid_api/models/credit_payroll_income_refresh_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_payroll_income_risk_signals_get(body: CreditPayrollIncomeRiskSignalsGetRequest | CreditPayrollIncomeRiskSignalsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditPayrollIncomeRiskSignalsGetResponse</code></summary>

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
try:
    response = client.credit_payroll_income_risk_signals_get(CreditPayrollIncomeRiskSignalsGetRequest())
    # TODO: Handle 'response' of type CreditPayrollIncomeRiskSignalsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_payroll_income_risk_signals_get(CreditPayrollIncomeRiskSignalsGetRequest())
    # TODO: Handle 'response' of type CreditPayrollIncomeRiskSignalsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditPayrollIncomeRiskSignalsGetResponse](the_plaid_api/models/credit_payroll_income_risk_signals_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_create(body: CreditRelayCreateRequest | CreditRelayCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditRelayCreateResponse</code></summary>

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
try:
    response = client.credit_relay_create(
        CreditRelayCreateRequest(report_tokens=["some example string"], secondary_client_id="some example string")
    )
    # TODO: Handle 'response' of type CreditRelayCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_relay_create(
        CreditRelayCreateRequest(report_tokens=["some example string"], secondary_client_id="some example string")
    )
    # TODO: Handle 'response' of type CreditRelayCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditRelayCreateResponse](the_plaid_api/models/credit_relay_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_get(body: CreditRelayGetRequest | CreditRelayGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportGetResponse</code></summary>

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
try:
    response = client.credit_relay_get(
        CreditRelayGetRequest(relay_token="some example string", report_type=ReportType.ASSET)
    )
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_relay_get(
        CreditRelayGetRequest(relay_token="some example string", report_type=ReportType.ASSET)
    )
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_pdf_get(body: CreditRelayPdfgetRequest | CreditRelayPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.credit_relay_pdf_get(
        CreditRelayPdfgetRequest(relay_token="some example string", report_type=ReportType.ASSET)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.credit_relay_pdf_get(
        CreditRelayPdfgetRequest(relay_token="some example string", report_type=ReportType.ASSET)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_refresh(body: CreditRelayRefreshRequest | CreditRelayRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditRelayRefreshResponse</code></summary>

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
try:
    response = client.credit_relay_refresh(
        CreditRelayRefreshRequest(relay_token="some example string", report_type=ReportType.ASSET)
    )
    # TODO: Handle 'response' of type CreditRelayRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_relay_refresh(
        CreditRelayRefreshRequest(relay_token="some example string", report_type=ReportType.ASSET)
    )
    # TODO: Handle 'response' of type CreditRelayRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditRelayRefreshResponse](the_plaid_api/models/credit_relay_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_relay_remove(body: CreditRelayRemoveRequest | CreditRelayRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditRelayRemoveResponse</code></summary>

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
try:
    response = client.credit_relay_remove(CreditRelayRemoveRequest(relay_token="some example string"))
    # TODO: Handle 'response' of type CreditRelayRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_relay_remove(CreditRelayRemoveRequest(relay_token="some example string"))
    # TODO: Handle 'response' of type CreditRelayRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditRelayRemoveResponse](the_plaid_api/models/credit_relay_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_report_audit_copy_remove(body: CreditAuditCopyTokenRemoveRequest | CreditAuditCopyTokenRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditAuditCopyTokenRemoveResponse</code></summary>

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
try:
    response = client.credit_report_audit_copy_remove(
        CreditAuditCopyTokenRemoveRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type CreditAuditCopyTokenRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_report_audit_copy_remove(
        CreditAuditCopyTokenRemoveRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type CreditAuditCopyTokenRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditAuditCopyTokenRemoveResponse](the_plaid_api/models/credit_audit_copy_token_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_sessions_get(body: CreditSessionsGetRequest | CreditSessionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreditSessionsGetResponse</code></summary>

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
try:
    response = client.credit_sessions_get(CreditSessionsGetRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CreditSessionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.credit_sessions_get(CreditSessionsGetRequest(user_token="some example string"))
    # TODO: Handle 'response' of type CreditSessionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreditSessionsGetResponse](the_plaid_api/models/credit_sessions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dashboard_user_get(body: DashboardUserGetRequest | DashboardUserGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DashboardUserGetResponse</code></summary>

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
try:
    response = client.dashboard_user_get(DashboardUserGetRequest(dashboard_user_id="some example string"))
    # TODO: Handle 'response' of type DashboardUserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dashboard_user_get(DashboardUserGetRequest(dashboard_user_id="some example string"))
    # TODO: Handle 'response' of type DashboardUserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[DashboardUserGetResponse](the_plaid_api/models/dashboard_user_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dashboard_user_list(body: DashboardUserListRequest | DashboardUserListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DashboardUserListResponse</code></summary>

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
try:
    response = client.dashboard_user_list(DashboardUserListRequest())
    # TODO: Handle 'response' of type DashboardUserListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dashboard_user_list(DashboardUserListRequest())
    # TODO: Handle 'response' of type DashboardUserListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[DashboardUserListResponse](the_plaid_api/models/dashboard_user_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def employers_search(body: EmployersSearchRequest | EmployersSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> EmployersSearchResponse</code></summary>

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
try:
    response = client.employers_search(
        EmployersSearchRequest(query="some example string", products=["some example string"])
    )
    # TODO: Handle 'response' of type EmployersSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.employers_search(
        EmployersSearchRequest(query="some example string", products=["some example string"])
    )
    # TODO: Handle 'response' of type EmployersSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[EmployersSearchResponse](the_plaid_api/models/employers_search_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def employment_verification_get(body: EmploymentVerificationGetRequest | EmploymentVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> EmploymentVerificationGetResponse</code></summary>

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
try:
    response = client.employment_verification_get(EmploymentVerificationGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type EmploymentVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.employment_verification_get(
        EmploymentVerificationGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type EmploymentVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[EmploymentVerificationGetResponse](the_plaid_api/models/employment_verification_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_get(consent_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FdxconsentGrant</code></summary>

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
try:
    response = client.fdx_consents_get("some example string")
    # TODO: Handle 'response' of type FdxconsentGrant
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.fdx_consents_get("some example string")
    # TODO: Handle 'response' of type FdxconsentGrant
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[FdxconsentGrant](the_plaid_api/models/fdxconsent_grant.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_list(customer_id: str, *, status: FdxConsentGrantStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetConsentsResponse</code></summary>

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
try:
    response = client.fdx_consents_list("some example string")
    # TODO: Handle 'response' of type GetConsentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.fdx_consents_list("some example string")
    # TODO: Handle 'response' of type GetConsentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GetConsentsResponse](the_plaid_api/models/get_consents_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_revocation_get(consent_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FdxconsentRevocations</code></summary>

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
try:
    response = client.fdx_consents_revocation_get("some example string")
    # TODO: Handle 'response' of type FdxconsentRevocations
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.fdx_consents_revocation_get("some example string")
    # TODO: Handle 'response' of type FdxconsentRevocations
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[FdxconsentRevocations](the_plaid_api/models/fdxconsent_revocations.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_consents_revoke(consent_id: str, body: FdxconsentRevocation | FdxconsentRevocationDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.fdx_consents_revoke(
        "some example string",
        FdxconsentRevocation(initiator=PartyType.DATA_ACCESS_PLATFORM, reason=FdxUpdateReason.BUSINESS_RULE),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.fdx_consents_revoke(
        "some example string",
        FdxconsentRevocation(initiator=PartyType.DATA_ACCESS_PLATFORM, reason=FdxUpdateReason.BUSINESS_RULE),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fdx_notifications(body: FdxNotificationEntity | FdxNotificationEntityDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.fdx_notifications(
        FdxNotificationEntity(
            notification_id="some example string",
            type_=NotificationType.ACCOUNT_TAKEOVER,
            sent_on=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
            category=NotificationCategory.SECURITY,
            notification_payload=NotificationPayloadEntity(),
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.fdx_notifications(
        FdxNotificationEntity(
            notification_id="some example string",
            type_=NotificationType.ACCOUNT_TAKEOVER,
            sent_on=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
            category=NotificationCategory.SECURITY,
            notification_payload=NotificationPayloadEntity(),
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recipient(recipient_id: str, *, oauth_state_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> FdxrecipientMetadata</code></summary>

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
try:
    response = client.get_recipient("some example string")
    # TODO: Handle 'response' of type FdxrecipientMetadata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.get_recipient("some example string")
    # TODO: Handle 'response' of type FdxrecipientMetadata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[FdxrecipientMetadata](the_plaid_api/models/fdxrecipient_metadata.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recipients(*, request_options: RequestOptionsOrDict | None = None) -> GetRecipientsResponse</code></summary>

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
try:
    response = client.get_recipients()
    # TODO: Handle 'response' of type GetRecipientsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.get_recipients()
    # TODO: Handle 'response' of type GetRecipientsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GetRecipientsResponse](the_plaid_api/models/get_recipients_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_documents_uploads_get(body: IdentityDocumentsUploadsGetRequest | IdentityDocumentsUploadsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityDocumentsUploadsGetResponse</code></summary>

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
try:
    response = client.identity_documents_uploads_get(
        IdentityDocumentsUploadsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type IdentityDocumentsUploadsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_documents_uploads_get(
        IdentityDocumentsUploadsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type IdentityDocumentsUploadsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityDocumentsUploadsGetResponse](the_plaid_api/models/identity_documents_uploads_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_get(body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityGetResponse</code></summary>

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
try:
    response = client.identity_get(IdentityGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_get(IdentityGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityGetResponse](the_plaid_api/models/identity_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_match(body: IdentityMatchRequest | IdentityMatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityMatchResponse</code></summary>

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
try:
    response = client.identity_match(IdentityMatchRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityMatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_match(IdentityMatchRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityMatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityMatchResponse](the_plaid_api/models/identity_match_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_refresh(body: IdentityRefreshRequest | IdentityRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityRefreshResponse</code></summary>

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
try:
    response = client.identity_refresh(IdentityRefreshRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_refresh(IdentityRefreshRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityRefreshResponse](the_plaid_api/models/identity_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_autofill_create(body: IdentityVerificationAutofillCreateRequest | IdentityVerificationAutofillCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityVerificationAutofillCreateResponse</code></summary>

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
try:
    response = client.identity_verification_autofill_create(
        IdentityVerificationAutofillCreateRequest(identity_verification_id="flwses_42cF1MNo42r9Xj")
    )
    # TODO: Handle 'response' of type IdentityVerificationAutofillCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_verification_autofill_create(
        IdentityVerificationAutofillCreateRequest(identity_verification_id="flwses_42cF1MNo42r9Xj")
    )
    # TODO: Handle 'response' of type IdentityVerificationAutofillCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityVerificationAutofillCreateResponse](the_plaid_api/models/identity_verification_autofill_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_create(body: IdentityVerificationCreateRequest | IdentityVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityVerificationCreateResponse</code></summary>

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
try:
    response = client.identity_verification_create(
        IdentityVerificationCreateRequest(is_shareable=True, template_id="some example string", gave_consent=True)
    )
    # TODO: Handle 'response' of type IdentityVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_verification_create(
        IdentityVerificationCreateRequest(is_shareable=True, template_id="some example string", gave_consent=True)
    )
    # TODO: Handle 'response' of type IdentityVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityVerificationCreateResponse](the_plaid_api/models/identity_verification_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_get(body: IdentityVerificationGetRequest | IdentityVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityVerificationGetResponse</code></summary>

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
try:
    response = client.identity_verification_get(
        IdentityVerificationGetRequest(identity_verification_id="some example string")
    )
    # TODO: Handle 'response' of type IdentityVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_verification_get(
        IdentityVerificationGetRequest(identity_verification_id="some example string")
    )
    # TODO: Handle 'response' of type IdentityVerificationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityVerificationGetResponse](the_plaid_api/models/identity_verification_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_list(body: IdentityVerificationListRequest | IdentityVerificationListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityVerificationListResponse</code></summary>

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
try:
    response = client.identity_verification_list(IdentityVerificationListRequest(template_id="some example string"))
    # TODO: Handle 'response' of type IdentityVerificationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_verification_list(
        IdentityVerificationListRequest(template_id="some example string")
    )
    # TODO: Handle 'response' of type IdentityVerificationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityVerificationListResponse](the_plaid_api/models/identity_verification_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def identity_verification_retry(body: IdentityVerificationRetryRequest | IdentityVerificationRetryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityVerificationRetryResponse</code></summary>

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
try:
    response = client.identity_verification_retry(
        IdentityVerificationRetryRequest(
            client_user_id="some example string", template_id="some example string", strategy=Strategy.RESET
        ),
    )
    # TODO: Handle 'response' of type IdentityVerificationRetryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity_verification_retry(
        IdentityVerificationRetryRequest(
            client_user_id="some example string", template_id="some example string", strategy=Strategy.RESET
        ),
    )
    # TODO: Handle 'response' of type IdentityVerificationRetryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IdentityVerificationRetryResponse](the_plaid_api/models/identity_verification_retry_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_create(body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationCreateResponse</code></summary>

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
try:
    response = client.income_verification_create(IncomeVerificationCreateRequest(webhook="some example string"))
    # TODO: Handle 'response' of type IncomeVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income_verification_create(
        IncomeVerificationCreateRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type IncomeVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IncomeVerificationCreateResponse](the_plaid_api/models/income_verification_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_documents_download(body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.income_verification_documents_download(IncomeVerificationDocumentsDownloadRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.income_verification_documents_download(IncomeVerificationDocumentsDownloadRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_paystubs_get(body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationPaystubsGetResponse</code></summary>

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
try:
    response = client.income_verification_paystubs_get(IncomeVerificationPaystubsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationPaystubsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income_verification_paystubs_get(IncomeVerificationPaystubsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationPaystubsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IncomeVerificationPaystubsGetResponse](the_plaid_api/models/income_verification_paystubs_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_precheck(body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationPrecheckResponse</code></summary>

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
try:
    response = client.income_verification_precheck(IncomeVerificationPrecheckRequest())
    # TODO: Handle 'response' of type IncomeVerificationPrecheckResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income_verification_precheck(IncomeVerificationPrecheckRequest())
    # TODO: Handle 'response' of type IncomeVerificationPrecheckResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IncomeVerificationPrecheckResponse](the_plaid_api/models/income_verification_precheck_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_taxforms_get(body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationTaxformsGetResponse</code></summary>

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
try:
    response = client.income_verification_taxforms_get(IncomeVerificationTaxformsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationTaxformsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income_verification_taxforms_get(IncomeVerificationTaxformsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationTaxformsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IncomeVerificationTaxformsGetResponse](the_plaid_api/models/income_verification_taxforms_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_get(body: InstitutionsGetRequest | InstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InstitutionsGetResponse</code></summary>

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
try:
    response = client.institutions_get(InstitutionsGetRequest(count=1, offset=1, country_codes=[CountryCode.US]))
    # TODO: Handle 'response' of type InstitutionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.institutions_get(
        InstitutionsGetRequest(count=1, offset=1, country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[InstitutionsGetResponse](the_plaid_api/models/institutions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_get_by_id(body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InstitutionsGetByIdResponse</code></summary>

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
try:
    response = client.institutions_get_by_id(
        InstitutionsGetByIdRequest(institution_id="some example string", country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsGetByIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.institutions_get_by_id(
        InstitutionsGetByIdRequest(institution_id="some example string", country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsGetByIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[InstitutionsGetByIdResponse](the_plaid_api/models/institutions_get_by_id_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_search(body: InstitutionsSearchRequest | InstitutionsSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InstitutionsSearchResponse</code></summary>

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
try:
    response = client.institutions_search(
        InstitutionsSearchRequest(query="some example string", country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.institutions_search(
        InstitutionsSearchRequest(query="some example string", country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[InstitutionsSearchResponse](the_plaid_api/models/institutions_search_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_auth_get(body: InvestmentsAuthGetRequest | InvestmentsAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InvestmentsAuthGetResponse</code></summary>

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
try:
    response = client.investments_auth_get(InvestmentsAuthGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type InvestmentsAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.investments_auth_get(InvestmentsAuthGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type InvestmentsAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[InvestmentsAuthGetResponse](the_plaid_api/models/investments_auth_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_holdings_get(body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InvestmentsHoldingsGetResponse</code></summary>

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
try:
    response = client.investments_holdings_get(InvestmentsHoldingsGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type InvestmentsHoldingsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.investments_holdings_get(
        InvestmentsHoldingsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type InvestmentsHoldingsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[InvestmentsHoldingsGetResponse](the_plaid_api/models/investments_holdings_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_refresh(body: InvestmentsRefreshRequest | InvestmentsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InvestmentsRefreshResponse</code></summary>

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
try:
    response = client.investments_refresh(InvestmentsRefreshRequest(access_token="some example string"))
    # TODO: Handle 'response' of type InvestmentsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.investments_refresh(InvestmentsRefreshRequest(access_token="some example string"))
    # TODO: Handle 'response' of type InvestmentsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[InvestmentsRefreshResponse](the_plaid_api/models/investments_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_transactions_get(body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InvestmentsTransactionsGetResponse</code></summary>

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
try:
    response = client.investments_transactions_get(
        InvestmentsTransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type InvestmentsTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.investments_transactions_get(
        InvestmentsTransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type InvestmentsTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[InvestmentsTransactionsGetResponse](the_plaid_api/models/investments_transactions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issues_get(body: IssuesGetRequest | IssuesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IssuesGetResponse</code></summary>

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
try:
    response = client.issues_get(IssuesGetRequest(issue_id="some example string"))
    # TODO: Handle 'response' of type IssuesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.issues_get(IssuesGetRequest(issue_id="some example string"))
    # TODO: Handle 'response' of type IssuesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IssuesGetResponse](the_plaid_api/models/issues_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issues_search(body: IssuesSearchRequest | IssuesSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IssuesSearchResponse</code></summary>

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
try:
    response = client.issues_search(IssuesSearchRequest())
    # TODO: Handle 'response' of type IssuesSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.issues_search(IssuesSearchRequest())
    # TODO: Handle 'response' of type IssuesSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IssuesSearchResponse](the_plaid_api/models/issues_search_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issues_subscribe(body: IssuesSubscribeRequest | IssuesSubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IssuesSubscribeResponse</code></summary>

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
try:
    response = client.issues_subscribe(
        IssuesSubscribeRequest(issue_id="some example string", webhook="some example string")
    )
    # TODO: Handle 'response' of type IssuesSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.issues_subscribe(
        IssuesSubscribeRequest(issue_id="some example string", webhook="some example string")
    )
    # TODO: Handle 'response' of type IssuesSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IssuesSubscribeResponse](the_plaid_api/models/issues_subscribe_response.py)</code> -- Subscription was successful

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_access_token_invalidate(body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemAccessTokenInvalidateResponse</code></summary>

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
try:
    response = client.item_access_token_invalidate(ItemAccessTokenInvalidateRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemAccessTokenInvalidateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_access_token_invalidate(
        ItemAccessTokenInvalidateRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type ItemAccessTokenInvalidateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemAccessTokenInvalidateResponse](the_plaid_api/models/item_access_token_invalidate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_activity_list(body: ItemActivityListRequest | ItemActivityListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemActivityListResponse</code></summary>

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
try:
    response = client.item_activity_list(ItemActivityListRequest())
    # TODO: Handle 'response' of type ItemActivityListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_activity_list(ItemActivityListRequest())
    # TODO: Handle 'response' of type ItemActivityListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemActivityListResponse](the_plaid_api/models/item_activity_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_list(body: ItemApplicationListRequest | ItemApplicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemApplicationListResponse</code></summary>

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
try:
    response = client.item_application_list(ItemApplicationListRequest())
    # TODO: Handle 'response' of type ItemApplicationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_application_list(ItemApplicationListRequest())
    # TODO: Handle 'response' of type ItemApplicationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemApplicationListResponse](the_plaid_api/models/item_application_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_scopes_update(body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemApplicationScopesUpdateResponse</code></summary>

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
try:
    response = client.item_application_scopes_update(
        ItemApplicationScopesUpdateRequest(
            access_token="some example string",
            application_id="some example string",
            scopes=Scopes(),
            context=ScopesContext.ENROLLMENT,
        ),
    )
    # TODO: Handle 'response' of type ItemApplicationScopesUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_application_scopes_update(
        ItemApplicationScopesUpdateRequest(
            access_token="some example string",
            application_id="some example string",
            scopes=Scopes(),
            context=ScopesContext.ENROLLMENT,
        ),
    )
    # TODO: Handle 'response' of type ItemApplicationScopesUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemApplicationScopesUpdateResponse](the_plaid_api/models/item_application_scopes_update_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_unlink(body: ItemApplicationUnlinkRequest | ItemApplicationUnlinkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemApplicationUnlinkResponse</code></summary>

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
try:
    response = client.item_application_unlink(
        ItemApplicationUnlinkRequest(access_token="some example string", application_id="some example string")
    )
    # TODO: Handle 'response' of type ItemApplicationUnlinkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_application_unlink(
        ItemApplicationUnlinkRequest(access_token="some example string", application_id="some example string")
    )
    # TODO: Handle 'response' of type ItemApplicationUnlinkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemApplicationUnlinkResponse](the_plaid_api/models/item_application_unlink_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_create_public_token(body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemPublicTokenCreateResponse</code></summary>

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
try:
    response = client.item_create_public_token(ItemPublicTokenCreateRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_create_public_token(
        ItemPublicTokenCreateRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type ItemPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemPublicTokenCreateResponse](the_plaid_api/models/item_public_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_get(body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemGetResponse</code></summary>

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
try:
    response = client.item_get(ItemGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_get(ItemGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemGetResponse](the_plaid_api/models/item_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_import(body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemImportResponse</code></summary>

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
try:
    response = client.item_import(
        ItemImportRequest(
            products=[Products.ASSETS],
            user_auth=ItemImportRequestUserAuth(user_id="some example string", auth_token="some example string"),
        ),
    )
    # TODO: Handle 'response' of type ItemImportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_import(
        ItemImportRequest(
            products=[Products.ASSETS],
            user_auth=ItemImportRequestUserAuth(user_id="some example string", auth_token="some example string"),
        ),
    )
    # TODO: Handle 'response' of type ItemImportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemImportResponse](the_plaid_api/models/item_import_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_products_terminate(body: ItemProductsTerminateRequest | ItemProductsTerminateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemProductsTerminateResponse</code></summary>

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
try:
    response = client.item_products_terminate(
        ItemProductsTerminateRequest(
            access_token="some example string", reason_code=ProductsTerminateReasonCode.FRAUD_FIRST_PARTY
        ),
    )
    # TODO: Handle 'response' of type ItemProductsTerminateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_products_terminate(
        ItemProductsTerminateRequest(
            access_token="some example string", reason_code=ProductsTerminateReasonCode.FRAUD_FIRST_PARTY
        ),
    )
    # TODO: Handle 'response' of type ItemProductsTerminateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemProductsTerminateResponse](the_plaid_api/models/item_products_terminate_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_public_token_exchange(body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemPublicTokenExchangeResponse</code></summary>

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
try:
    response = client.item_public_token_exchange(ItemPublicTokenExchangeRequest(public_token="some example string"))
    # TODO: Handle 'response' of type ItemPublicTokenExchangeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_public_token_exchange(
        ItemPublicTokenExchangeRequest(public_token="some example string")
    )
    # TODO: Handle 'response' of type ItemPublicTokenExchangeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemPublicTokenExchangeResponse](the_plaid_api/models/item_public_token_exchange_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_remove(body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemRemoveResponse</code></summary>

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
try:
    response = client.item_remove(ItemRemoveRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_remove(ItemRemoveRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemRemoveResponse](the_plaid_api/models/item_remove_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_webhook_update(body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemWebhookUpdateResponse</code></summary>

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
try:
    response = client.item_webhook_update(ItemWebhookUpdateRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_webhook_update(ItemWebhookUpdateRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ItemWebhookUpdateResponse](the_plaid_api/models/item_webhook_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def liabilities_get(body: LiabilitiesGetRequest | LiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LiabilitiesGetResponse</code></summary>

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
try:
    response = client.liabilities_get(LiabilitiesGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type LiabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.liabilities_get(LiabilitiesGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type LiabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LiabilitiesGetResponse](the_plaid_api/models/liabilities_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_delivery_create(body: LinkDeliveryCreateRequest | LinkDeliveryCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LinkDeliveryCreateResponse</code></summary>

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
try:
    response = client.link_delivery_create(LinkDeliveryCreateRequest(link_token="some example string"))
    # TODO: Handle 'response' of type LinkDeliveryCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.link_delivery_create(LinkDeliveryCreateRequest(link_token="some example string"))
    # TODO: Handle 'response' of type LinkDeliveryCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LinkDeliveryCreateResponse](the_plaid_api/models/link_delivery_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_delivery_get(body: LinkDeliveryGetRequest | LinkDeliveryGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LinkDeliveryGetResponse</code></summary>

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
try:
    response = client.link_delivery_get(LinkDeliveryGetRequest(link_delivery_session_id="some example string"))
    # TODO: Handle 'response' of type LinkDeliveryGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.link_delivery_get(
        LinkDeliveryGetRequest(link_delivery_session_id="some example string")
    )
    # TODO: Handle 'response' of type LinkDeliveryGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LinkDeliveryGetResponse](the_plaid_api/models/link_delivery_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_oauth_correlation_id_exchange(body: LinkOauthCorrelationIdExchangeRequest | LinkOauthCorrelationIdExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LinkOauthCorrelationIdExchangeResponse</code></summary>

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
try:
    response = client.link_oauth_correlation_id_exchange(
        LinkOauthCorrelationIdExchangeRequest(link_correlation_id="some example string")
    )
    # TODO: Handle 'response' of type LinkOauthCorrelationIdExchangeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.link_oauth_correlation_id_exchange(
        LinkOauthCorrelationIdExchangeRequest(link_correlation_id="some example string")
    )
    # TODO: Handle 'response' of type LinkOauthCorrelationIdExchangeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LinkOauthCorrelationIdExchangeResponse](the_plaid_api/models/link_oauth_correlation_id_exchange_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_token_create(body: LinkTokenCreateRequest | LinkTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LinkTokenCreateResponse</code></summary>

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
try:
    response = client.link_token_create(
        LinkTokenCreateRequest(
            client_name="some example string", language="some example string", country_codes=[CountryCode.US]
        ),
    )
    # TODO: Handle 'response' of type LinkTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.link_token_create(
        LinkTokenCreateRequest(
            client_name="some example string", language="some example string", country_codes=[CountryCode.US]
        ),
    )
    # TODO: Handle 'response' of type LinkTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LinkTokenCreateResponse](the_plaid_api/models/link_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_token_get(body: LinkTokenGetRequest | LinkTokenGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LinkTokenGetResponse</code></summary>

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
try:
    response = client.link_token_get(LinkTokenGetRequest(link_token="some example string"))
    # TODO: Handle 'response' of type LinkTokenGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.link_token_get(LinkTokenGetRequest(link_token="some example string"))
    # TODO: Handle 'response' of type LinkTokenGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LinkTokenGetResponse](the_plaid_api/models/link_token_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def network_status_get(body: NetworkStatusGetRequest | NetworkStatusGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> NetworkStatusGetResponse</code></summary>

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
try:
    response = client.network_status_get(
        NetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
    )
    # TODO: Handle 'response' of type NetworkStatusGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.network_status_get(
        NetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
    )
    # TODO: Handle 'response' of type NetworkStatusGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[NetworkStatusGetResponse](the_plaid_api/models/network_status_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_introspect(body: OauthIntrospectRequest | OauthIntrospectRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> OauthIntrospectResponse</code></summary>

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
try:
    response = client.oauth_introspect(OauthIntrospectRequest(token="some example string"))
    # TODO: Handle 'response' of type OauthIntrospectResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.oauth_introspect(OauthIntrospectRequest(token="some example string"))
    # TODO: Handle 'response' of type OauthIntrospectResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[OauthIntrospectResponse](the_plaid_api/models/oauth_introspect_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_revoke(body: OauthRevokeRequest | OauthRevokeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> OauthRevokeResponse</code></summary>

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
try:
    response = client.oauth_revoke(OauthRevokeRequest(token="some example string"))
    # TODO: Handle 'response' of type OauthRevokeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.oauth_revoke(OauthRevokeRequest(token="some example string"))
    # TODO: Handle 'response' of type OauthRevokeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[OauthRevokeResponse](the_plaid_api/models/oauth_revoke_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_token(body: OauthTokenRequest | OauthTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> OauthTokenResponse</code></summary>

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
try:
    response = client.oauth_token(OauthTokenRequest(grant_type=OauthGrantType.REFRESH_TOKEN))
    # TODO: Handle 'response' of type OauthTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.oauth_token(OauthTokenRequest(grant_type=OauthGrantType.REFRESH_TOKEN))
    # TODO: Handle 'response' of type OauthTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[OauthTokenResponse](the_plaid_api/models/oauth_token_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_create(body: PartnerCustomerCreateRequest | PartnerCustomerCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PartnerCustomerCreateResponse</code></summary>

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
try:
    response = client.partner_customer_create(
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
    # TODO: Handle 'response' of type PartnerCustomerCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner_customer_create(
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
    # TODO: Handle 'response' of type PartnerCustomerCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PartnerCustomerCreateResponse](the_plaid_api/models/partner_customer_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_enable(body: PartnerCustomerEnableRequest | PartnerCustomerEnableRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PartnerCustomerEnableResponse</code></summary>

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
try:
    response = client.partner_customer_enable(
        PartnerCustomerEnableRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner_customer_enable(
        PartnerCustomerEnableRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PartnerCustomerEnableResponse](the_plaid_api/models/partner_customer_enable_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_get(body: PartnerCustomerGetRequest | PartnerCustomerGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PartnerCustomerGetResponse</code></summary>

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
try:
    response = client.partner_customer_get(
        PartnerCustomerGetRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner_customer_get(
        PartnerCustomerGetRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PartnerCustomerGetResponse](the_plaid_api/models/partner_customer_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_oauth_institutions_get(body: PartnerCustomerOauthInstitutionsGetRequest | PartnerCustomerOauthInstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PartnerCustomerOauthInstitutionsGetResponse</code></summary>

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
try:
    response = client.partner_customer_oauth_institutions_get(
        PartnerCustomerOauthInstitutionsGetRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerOauthInstitutionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner_customer_oauth_institutions_get(
        PartnerCustomerOauthInstitutionsGetRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerOauthInstitutionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PartnerCustomerOauthInstitutionsGetResponse](the_plaid_api/models/partner_customer_oauth_institutions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def partner_customer_remove(body: PartnerCustomerRemoveRequest | PartnerCustomerRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PartnerCustomerRemoveResponse</code></summary>

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
try:
    response = client.partner_customer_remove(
        PartnerCustomerRemoveRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner_customer_remove(
        PartnerCustomerRemoveRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
        ),
    )
    # TODO: Handle 'response' of type PartnerCustomerRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PartnerCustomerRemoveResponse](the_plaid_api/models/partner_customer_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_create(body: PaymentInitiationConsentCreateRequest | PaymentInitiationConsentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationConsentCreateResponse</code></summary>

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
try:
    response = client.payment_initiation_consent_create(
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
    # TODO: Handle 'response' of type PaymentInitiationConsentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_consent_create(
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
    # TODO: Handle 'response' of type PaymentInitiationConsentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationConsentCreateResponse](the_plaid_api/models/payment_initiation_consent_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_get(body: PaymentInitiationConsentGetRequest | PaymentInitiationConsentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationConsentGetResponse</code></summary>

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
try:
    response = client.payment_initiation_consent_get(
        PaymentInitiationConsentGetRequest(consent_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationConsentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_consent_get(
        PaymentInitiationConsentGetRequest(consent_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationConsentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationConsentGetResponse](the_plaid_api/models/payment_initiation_consent_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_payment_execute(body: PaymentInitiationConsentPaymentExecuteRequest | PaymentInitiationConsentPaymentExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationConsentPaymentExecuteResponse</code></summary>

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
try:
    response = client.payment_initiation_consent_payment_execute(
        PaymentInitiationConsentPaymentExecuteRequest(
            consent_id="some example string",
            amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
            idempotency_key="some example string",
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationConsentPaymentExecuteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_consent_payment_execute(
        PaymentInitiationConsentPaymentExecuteRequest(
            consent_id="some example string",
            amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
            idempotency_key="some example string",
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationConsentPaymentExecuteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationConsentPaymentExecuteResponse](the_plaid_api/models/payment_initiation_consent_payment_execute_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_consent_revoke(body: PaymentInitiationConsentRevokeRequest | PaymentInitiationConsentRevokeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationConsentRevokeResponse</code></summary>

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
try:
    response = client.payment_initiation_consent_revoke(
        PaymentInitiationConsentRevokeRequest(consent_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationConsentRevokeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_consent_revoke(
        PaymentInitiationConsentRevokeRequest(consent_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationConsentRevokeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationConsentRevokeResponse](the_plaid_api/models/payment_initiation_consent_revoke_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_create(body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentCreateResponse</code></summary>

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
try:
    response = client.payment_initiation_payment_create(
        PaymentInitiationPaymentCreateRequest(
            recipient_id="some example string",
            reference="some example string",
            amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_payment_create(
        PaymentInitiationPaymentCreateRequest(
            recipient_id="some example string",
            reference="some example string",
            amount=PaymentAmount(currency=PaymentAmountCurrency.GBP, value=1.5),
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationPaymentCreateResponse](the_plaid_api/models/payment_initiation_payment_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_get(body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentGetResponse</code></summary>

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
try:
    response = client.payment_initiation_payment_get(
        PaymentInitiationPaymentGetRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_payment_get(
        PaymentInitiationPaymentGetRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationPaymentGetResponse](the_plaid_api/models/payment_initiation_payment_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_list(body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentListResponse</code></summary>

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
try:
    response = client.payment_initiation_payment_list(PaymentInitiationPaymentListRequest())
    # TODO: Handle 'response' of type PaymentInitiationPaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_payment_list(PaymentInitiationPaymentListRequest())
    # TODO: Handle 'response' of type PaymentInitiationPaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationPaymentListResponse](the_plaid_api/models/payment_initiation_payment_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_reverse(body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentReverseResponse</code></summary>

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
try:
    response = client.payment_initiation_payment_reverse(
        PaymentInitiationPaymentReverseRequest(
            payment_id="some example string", idempotency_key="some example string", reference="some example string"
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentReverseResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_payment_reverse(
        PaymentInitiationPaymentReverseRequest(
            payment_id="some example string", idempotency_key="some example string", reference="some example string"
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentReverseResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationPaymentReverseResponse](the_plaid_api/models/payment_initiation_payment_reverse_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_create(body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationRecipientCreateResponse</code></summary>

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
try:
    response = client.payment_initiation_recipient_create(
        PaymentInitiationRecipientCreateRequest(name="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_recipient_create(
        PaymentInitiationRecipientCreateRequest(name="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationRecipientCreateResponse](the_plaid_api/models/payment_initiation_recipient_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_get(body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationRecipientGetResponse</code></summary>

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
try:
    response = client.payment_initiation_recipient_get(
        PaymentInitiationRecipientGetRequest(recipient_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_recipient_get(
        PaymentInitiationRecipientGetRequest(recipient_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationRecipientGetResponse](the_plaid_api/models/payment_initiation_recipient_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_list(body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationRecipientListResponse</code></summary>

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
try:
    response = client.payment_initiation_recipient_list(PaymentInitiationRecipientListRequest())
    # TODO: Handle 'response' of type PaymentInitiationRecipientListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation_recipient_list(PaymentInitiationRecipientListRequest())
    # TODO: Handle 'response' of type PaymentInitiationRecipientListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentInitiationRecipientListResponse](the_plaid_api/models/payment_initiation_recipient_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_profile_create(body: PaymentProfileCreateRequest | PaymentProfileCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileCreateResponse</code></summary>

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
try:
    response = client.payment_profile_create(PaymentProfileCreateRequest())
    # TODO: Handle 'response' of type PaymentProfileCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_profile_create(PaymentProfileCreateRequest())
    # TODO: Handle 'response' of type PaymentProfileCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentProfileCreateResponse](the_plaid_api/models/payment_profile_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_profile_get(body: PaymentProfileGetRequest | PaymentProfileGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileGetResponse</code></summary>

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
try:
    response = client.payment_profile_get(PaymentProfileGetRequest(payment_profile_token="some example string"))
    # TODO: Handle 'response' of type PaymentProfileGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_profile_get(
        PaymentProfileGetRequest(payment_profile_token="some example string")
    )
    # TODO: Handle 'response' of type PaymentProfileGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentProfileGetResponse](the_plaid_api/models/payment_profile_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_profile_remove(body: PaymentProfileRemoveRequest | PaymentProfileRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileRemoveResponse</code></summary>

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
try:
    response = client.payment_profile_remove(PaymentProfileRemoveRequest(payment_profile_token="some example string"))
    # TODO: Handle 'response' of type PaymentProfileRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_profile_remove(
        PaymentProfileRemoveRequest(payment_profile_token="some example string")
    )
    # TODO: Handle 'response' of type PaymentProfileRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PaymentProfileRemoveResponse](the_plaid_api/models/payment_profile_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_account_get(body: ProcessorAccountGetRequest | ProcessorAccountGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorAccountGetResponse</code></summary>

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
try:
    response = client.processor_account_get(ProcessorAccountGetRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorAccountGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_account_get(
        ProcessorAccountGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorAccountGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorAccountGetResponse](the_plaid_api/models/processor_account_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_apex_processor_token_create(body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTokenCreateResponse</code></summary>

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
try:
    response = client.processor_apex_processor_token_create(
        ProcessorApexProcessorTokenCreateRequest(access_token="some example string", account_id="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_apex_processor_token_create(
        ProcessorApexProcessorTokenCreateRequest(access_token="some example string", account_id="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_auth_get(body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorAuthGetResponse</code></summary>

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
try:
    response = client.processor_auth_get(ProcessorAuthGetRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_auth_get(ProcessorAuthGetRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorAuthGetResponse](the_plaid_api/models/processor_auth_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_balance_get(body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorBalanceGetResponse</code></summary>

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
try:
    response = client.processor_balance_get(ProcessorBalanceGetRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_balance_get(
        ProcessorBalanceGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorBalanceGetResponse](the_plaid_api/models/processor_balance_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_bank_transfer_create(body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorBankTransferCreateResponse</code></summary>

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
try:
    response = client.processor_bank_transfer_create(
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
    # TODO: Handle 'response' of type ProcessorBankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_bank_transfer_create(
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
    # TODO: Handle 'response' of type ProcessorBankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorBankTransferCreateResponse](the_plaid_api/models/processor_bank_transfer_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_identity_get(body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorIdentityGetResponse</code></summary>

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
try:
    response = client.processor_identity_get(ProcessorIdentityGetRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorIdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_identity_get(
        ProcessorIdentityGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorIdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorIdentityGetResponse](the_plaid_api/models/processor_identity_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_identity_match(body: ProcessorIdentityMatchRequest | ProcessorIdentityMatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorIdentityMatchResponse</code></summary>

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
try:
    response = client.processor_identity_match(ProcessorIdentityMatchRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorIdentityMatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_identity_match(
        ProcessorIdentityMatchRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorIdentityMatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorIdentityMatchResponse](the_plaid_api/models/processor_identity_match_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_investments_auth_get(body: ProcessorInvestmentsAuthGetRequest | ProcessorInvestmentsAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorInvestmentsAuthGetResponse</code></summary>

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
try:
    response = client.processor_investments_auth_get(
        ProcessorInvestmentsAuthGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorInvestmentsAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_investments_auth_get(
        ProcessorInvestmentsAuthGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorInvestmentsAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorInvestmentsAuthGetResponse](the_plaid_api/models/processor_investments_auth_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_investments_holdings_get(body: ProcessorInvestmentsHoldingsGetRequest | ProcessorInvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorInvestmentsHoldingsGetResponse</code></summary>

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
try:
    response = client.processor_investments_holdings_get(
        ProcessorInvestmentsHoldingsGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorInvestmentsHoldingsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_investments_holdings_get(
        ProcessorInvestmentsHoldingsGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorInvestmentsHoldingsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorInvestmentsHoldingsGetResponse](the_plaid_api/models/processor_investments_holdings_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_investments_transactions_get(body: ProcessorInvestmentsTransactionsGetRequest | ProcessorInvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorInvestmentsTransactionsGetResponse</code></summary>

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
try:
    response = client.processor_investments_transactions_get(
        ProcessorInvestmentsTransactionsGetRequest(
            processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type ProcessorInvestmentsTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_investments_transactions_get(
        ProcessorInvestmentsTransactionsGetRequest(
            processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type ProcessorInvestmentsTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorInvestmentsTransactionsGetResponse](the_plaid_api/models/processor_investments_transactions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_liabilities_get(body: ProcessorLiabilitiesGetRequest | ProcessorLiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorLiabilitiesGetResponse</code></summary>

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
try:
    response = client.processor_liabilities_get(ProcessorLiabilitiesGetRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorLiabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_liabilities_get(
        ProcessorLiabilitiesGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorLiabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorLiabilitiesGetResponse](the_plaid_api/models/processor_liabilities_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_decision_report(body: ProcessorSignalDecisionReportRequest | ProcessorSignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorSignalDecisionReportResponse</code></summary>

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
try:
    response = client.processor_signal_decision_report(
        ProcessorSignalDecisionReportRequest(
            processor_token="some example string", client_transaction_id="some example string", initiated=True
        ),
    )
    # TODO: Handle 'response' of type ProcessorSignalDecisionReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_signal_decision_report(
        ProcessorSignalDecisionReportRequest(
            processor_token="some example string", client_transaction_id="some example string", initiated=True
        ),
    )
    # TODO: Handle 'response' of type ProcessorSignalDecisionReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorSignalDecisionReportResponse](the_plaid_api/models/processor_signal_decision_report_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_evaluate(body: ProcessorSignalEvaluateRequest | ProcessorSignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorSignalEvaluateResponse</code></summary>

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
try:
    response = client.processor_signal_evaluate(
        ProcessorSignalEvaluateRequest(
            processor_token="some example string", client_transaction_id="some example string", amount=1.5
        ),
    )
    # TODO: Handle 'response' of type ProcessorSignalEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_signal_evaluate(
        ProcessorSignalEvaluateRequest(
            processor_token="some example string", client_transaction_id="some example string", amount=1.5
        ),
    )
    # TODO: Handle 'response' of type ProcessorSignalEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorSignalEvaluateResponse](the_plaid_api/models/processor_signal_evaluate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_prepare(body: ProcessorSignalPrepareRequest | ProcessorSignalPrepareRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorSignalPrepareResponse</code></summary>

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
try:
    response = client.processor_signal_prepare(ProcessorSignalPrepareRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorSignalPrepareResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_signal_prepare(
        ProcessorSignalPrepareRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorSignalPrepareResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorSignalPrepareResponse](the_plaid_api/models/processor_signal_prepare_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_signal_return_report(body: ProcessorSignalReturnReportRequest | ProcessorSignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorSignalReturnReportResponse</code></summary>

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
try:
    response = client.processor_signal_return_report(
        ProcessorSignalReturnReportRequest(
            processor_token="some example string",
            client_transaction_id="some example string",
            return_code="some example string",
        ),
    )
    # TODO: Handle 'response' of type ProcessorSignalReturnReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_signal_return_report(
        ProcessorSignalReturnReportRequest(
            processor_token="some example string",
            client_transaction_id="some example string",
            return_code="some example string",
        ),
    )
    # TODO: Handle 'response' of type ProcessorSignalReturnReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorSignalReturnReportResponse](the_plaid_api/models/processor_signal_return_report_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_stripe_bank_account_token_create(body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorStripeBankAccountTokenCreateResponse</code></summary>

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
try:
    response = client.processor_stripe_bank_account_token_create(
        ProcessorStripeBankAccountTokenCreateRequest(
            access_token="some example string", account_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ProcessorStripeBankAccountTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_stripe_bank_account_token_create(
        ProcessorStripeBankAccountTokenCreateRequest(
            access_token="some example string", account_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ProcessorStripeBankAccountTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorStripeBankAccountTokenCreateResponse](the_plaid_api/models/processor_stripe_bank_account_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_create(body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTokenCreateResponse</code></summary>

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
try:
    response = client.processor_token_create(
        ProcessorTokenCreateRequest(
            access_token="some example string", account_id="some example string", processor=Processor.DWOLLA
        ),
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_token_create(
        ProcessorTokenCreateRequest(
            access_token="some example string", account_id="some example string", processor=Processor.DWOLLA
        ),
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_permissions_get(body: ProcessorTokenPermissionsGetRequest | ProcessorTokenPermissionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTokenPermissionsGetResponse</code></summary>

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
try:
    response = client.processor_token_permissions_get(
        ProcessorTokenPermissionsGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenPermissionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_token_permissions_get(
        ProcessorTokenPermissionsGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenPermissionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTokenPermissionsGetResponse](the_plaid_api/models/processor_token_permissions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_permissions_set(body: ProcessorTokenPermissionsSetRequest | ProcessorTokenPermissionsSetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTokenPermissionsSetResponse</code></summary>

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
try:
    response = client.processor_token_permissions_set(
        ProcessorTokenPermissionsSetRequest(processor_token="some example string", products=[Products.ASSETS])
    )
    # TODO: Handle 'response' of type ProcessorTokenPermissionsSetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_token_permissions_set(
        ProcessorTokenPermissionsSetRequest(processor_token="some example string", products=[Products.ASSETS])
    )
    # TODO: Handle 'response' of type ProcessorTokenPermissionsSetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTokenPermissionsSetResponse](the_plaid_api/models/processor_token_permissions_set_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_webhook_update(body: ProcessorTokenWebhookUpdateRequest | ProcessorTokenWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTokenWebhookUpdateResponse</code></summary>

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
try:
    response = client.processor_token_webhook_update(
        ProcessorTokenWebhookUpdateRequest(processor_token="some example string", webhook="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_token_webhook_update(
        ProcessorTokenWebhookUpdateRequest(processor_token="some example string", webhook="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTokenWebhookUpdateResponse](the_plaid_api/models/processor_token_webhook_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_get(body: ProcessorTransactionsGetRequest | ProcessorTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTransactionsGetResponse</code></summary>

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
try:
    response = client.processor_transactions_get(
        ProcessorTransactionsGetRequest(
            processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type ProcessorTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_transactions_get(
        ProcessorTransactionsGetRequest(
            processor_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type ProcessorTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTransactionsGetResponse](the_plaid_api/models/processor_transactions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_recurring_get(body: ProcessorTransactionsRecurringGetRequest | ProcessorTransactionsRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTransactionsRecurringGetResponse</code></summary>

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
try:
    response = client.processor_transactions_recurring_get(
        ProcessorTransactionsRecurringGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTransactionsRecurringGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_transactions_recurring_get(
        ProcessorTransactionsRecurringGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTransactionsRecurringGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTransactionsRecurringGetResponse](the_plaid_api/models/processor_transactions_recurring_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_refresh(body: ProcessorTransactionsRefreshRequest | ProcessorTransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTransactionsRefreshResponse</code></summary>

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
try:
    response = client.processor_transactions_refresh(
        ProcessorTransactionsRefreshRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_transactions_refresh(
        ProcessorTransactionsRefreshRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTransactionsRefreshResponse](the_plaid_api/models/processor_transactions_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_transactions_sync(body: ProcessorTransactionsSyncRequest | ProcessorTransactionsSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTransactionsSyncResponse</code></summary>

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
try:
    response = client.processor_transactions_sync(
        ProcessorTransactionsSyncRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTransactionsSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_transactions_sync(
        ProcessorTransactionsSyncRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTransactionsSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProcessorTransactionsSyncResponse](the_plaid_api/models/processor_transactions_sync_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def profile_network_status_get(body: ProfileNetworkStatusGetRequest | ProfileNetworkStatusGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProfileNetworkStatusGetResponse</code></summary>

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
try:
    response = client.profile_network_status_get(
        ProfileNetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
    )
    # TODO: Handle 'response' of type ProfileNetworkStatusGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.profile_network_status_get(
        ProfileNetworkStatusGetRequest(user=NetworkStatusGetUser(phone_number="some example string"))
    )
    # TODO: Handle 'response' of type ProfileNetworkStatusGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProfileNetworkStatusGetResponse](the_plaid_api/models/profile_network_status_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_compute(body: ProtectComputeRequest | ProtectComputeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProtectComputeResponse</code></summary>

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
try:
    response = client.protect_compute(ProtectComputeRequest(model="some example string", user=ProtectUser()))
    # TODO: Handle 'response' of type ProtectComputeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.protect_compute(
        ProtectComputeRequest(model="some example string", user=ProtectUser())
    )
    # TODO: Handle 'response' of type ProtectComputeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProtectComputeResponse](the_plaid_api/models/protect_compute_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_event_get(body: ProtectEventGetRequest | ProtectEventGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProtectEventGetResponse</code></summary>

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
try:
    response = client.protect_event_get(ProtectEventGetRequest(event_id="some example string"))
    # TODO: Handle 'response' of type ProtectEventGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.protect_event_get(ProtectEventGetRequest(event_id="some example string"))
    # TODO: Handle 'response' of type ProtectEventGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProtectEventGetResponse](the_plaid_api/models/protect_event_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_event_send(body: ProtectEventSendRequest | ProtectEventSendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProtectEventSendResponse</code></summary>

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
try:
    response = client.protect_event_send(
        ProtectEventSendRequest(event=ProtectEvent(timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)))
    )
    # TODO: Handle 'response' of type ProtectEventSendResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.protect_event_send(
        ProtectEventSendRequest(event=ProtectEvent(timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)))
    )
    # TODO: Handle 'response' of type ProtectEventSendResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProtectEventSendResponse](the_plaid_api/models/protect_event_send_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_report_create(body: ProtectReportCreateRequest | ProtectReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProtectReportCreateResponse</code></summary>

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
try:
    response = client.protect_report_create(
        ProtectReportCreateRequest(
            report_confidence=ProtectReportConfidence.CONFIRMED,
            report_type=ProtectReportType.USER_ACCOUNT_TAKEOVER,
            report_source=ProtectReportSource.INTERNAL_REVIEW,
        ),
    )
    # TODO: Handle 'response' of type ProtectReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.protect_report_create(
        ProtectReportCreateRequest(
            report_confidence=ProtectReportConfidence.CONFIRMED,
            report_type=ProtectReportType.USER_ACCOUNT_TAKEOVER,
            report_source=ProtectReportSource.INTERNAL_REVIEW,
        ),
    )
    # TODO: Handle 'response' of type ProtectReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProtectReportCreateResponse](the_plaid_api/models/protect_report_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def protect_user_insights_get(body: ProtectUserInsightsGetRequest | ProtectUserInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProtectUserInsightsGetResponse</code></summary>

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
try:
    response = client.protect_user_insights_get(ProtectUserInsightsGetRequest())
    # TODO: Handle 'response' of type ProtectUserInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.protect_user_insights_get(ProtectUserInsightsGetRequest())
    # TODO: Handle 'response' of type ProtectUserInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ProtectUserInsightsGetResponse](the_plaid_api/models/protect_user_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_bank_income_fire_webhook(body: SandboxBankIncomeFireWebhookRequest | SandboxBankIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxBankIncomeFireWebhookResponse</code></summary>

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
try:
    response = client.sandbox_bank_income_fire_webhook(
        SandboxBankIncomeFireWebhookRequest(
            webhook_code=SandboxBankIncomeWebhookFireRequestWebhookCode.BANK_INCOME_REFRESH_UPDATE,
            webhook_fields=SandboxBankIncomeWebhookFireRequestWebhookFields(user_id="some example string"),
        ),
    )
    # TODO: Handle 'response' of type SandboxBankIncomeFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_bank_income_fire_webhook(
        SandboxBankIncomeFireWebhookRequest(
            webhook_code=SandboxBankIncomeWebhookFireRequestWebhookCode.BANK_INCOME_REFRESH_UPDATE,
            webhook_fields=SandboxBankIncomeWebhookFireRequestWebhookFields(user_id="some example string"),
        ),
    )
    # TODO: Handle 'response' of type SandboxBankIncomeFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxBankIncomeFireWebhookResponse](the_plaid_api/models/sandbox_bank_income_fire_webhook_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_bank_transfer_fire_webhook(body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxBankTransferFireWebhookResponse</code></summary>

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
try:
    response = client.sandbox_bank_transfer_fire_webhook(
        SandboxBankTransferFireWebhookRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_bank_transfer_fire_webhook(
        SandboxBankTransferFireWebhookRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxBankTransferFireWebhookResponse](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_bank_transfer_simulate(body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxBankTransferSimulateResponse</code></summary>

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
try:
    response = client.sandbox_bank_transfer_simulate(
        SandboxBankTransferSimulateRequest(bank_transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_bank_transfer_simulate(
        SandboxBankTransferSimulateRequest(bank_transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxBankTransferSimulateResponse](the_plaid_api/models/sandbox_bank_transfer_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_cra_cashflow_updates_update(body: SandboxCraCashflowUpdatesUpdateRequest | SandboxCraCashflowUpdatesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxCraCashflowUpdatesUpdateResponse</code></summary>

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
try:
    response = client.sandbox_cra_cashflow_updates_update(SandboxCraCashflowUpdatesUpdateRequest())
    # TODO: Handle 'response' of type SandboxCraCashflowUpdatesUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_cra_cashflow_updates_update(SandboxCraCashflowUpdatesUpdateRequest())
    # TODO: Handle 'response' of type SandboxCraCashflowUpdatesUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxCraCashflowUpdatesUpdateResponse](the_plaid_api/models/sandbox_cra_cashflow_updates_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_fdx_consent_seed(body: SandboxFdxConsentSeedRequest | SandboxFdxConsentSeedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxFdxConsentSeedResponse</code></summary>

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
try:
    response = client.sandbox_fdx_consent_seed(
        SandboxFdxConsentSeedRequest(customer_id="some example string", application_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxFdxConsentSeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_fdx_consent_seed(
        SandboxFdxConsentSeedRequest(customer_id="some example string", application_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxFdxConsentSeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxFdxConsentSeedResponse](the_plaid_api/models/sandbox_fdx_consent_seed_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_income_fire_webhook(body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxIncomeFireWebhookResponse</code></summary>

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
try:
    response = client.sandbox_income_fire_webhook(
        SandboxIncomeFireWebhookRequest(
            item_id="some example string",
            webhook="some example string",
            webhook_code=SandboxIncomeWebhookFireRequestWebhookCode.INCOME_VERIFICATION,
        ),
    )
    # TODO: Handle 'response' of type SandboxIncomeFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_income_fire_webhook(
        SandboxIncomeFireWebhookRequest(
            item_id="some example string",
            webhook="some example string",
            webhook_code=SandboxIncomeWebhookFireRequestWebhookCode.INCOME_VERIFICATION,
        ),
    )
    # TODO: Handle 'response' of type SandboxIncomeFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxIncomeFireWebhookResponse](the_plaid_api/models/sandbox_income_fire_webhook_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_application_seed(body: SandboxItemApplicationSeedRequest | SandboxItemApplicationSeedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxItemApplicationSeedResponse</code></summary>

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
try:
    response = client.sandbox_item_application_seed(
        SandboxItemApplicationSeedRequest(access_token="some example string", application_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxItemApplicationSeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_item_application_seed(
        SandboxItemApplicationSeedRequest(access_token="some example string", application_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxItemApplicationSeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxItemApplicationSeedResponse](the_plaid_api/models/sandbox_item_application_seed_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_fire_webhook(body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxItemFireWebhookResponse</code></summary>

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
try:
    response = client.sandbox_item_fire_webhook(
        SandboxItemFireWebhookRequest(access_token="some example string", webhook_code=WebhookCode.DEFAULT_UPDATE)
    )
    # TODO: Handle 'response' of type SandboxItemFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_item_fire_webhook(
        SandboxItemFireWebhookRequest(access_token="some example string", webhook_code=WebhookCode.DEFAULT_UPDATE)
    )
    # TODO: Handle 'response' of type SandboxItemFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxItemFireWebhookResponse](the_plaid_api/models/sandbox_item_fire_webhook_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_reset_login(body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxItemResetLoginResponse</code></summary>

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
try:
    response = client.sandbox_item_reset_login(SandboxItemResetLoginRequest(access_token="some example string"))
    # TODO: Handle 'response' of type SandboxItemResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_item_reset_login(
        SandboxItemResetLoginRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type SandboxItemResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxItemResetLoginResponse](the_plaid_api/models/sandbox_item_reset_login_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_set_verification_status(body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxItemSetVerificationStatusResponse</code></summary>

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
try:
    response = client.sandbox_item_set_verification_status(
        SandboxItemSetVerificationStatusRequest(
            access_token="some example string",
            account_id="some example string",
            verification_status=VerificationStatus1.AUTOMATICALLY_VERIFIED,
        ),
    )
    # TODO: Handle 'response' of type SandboxItemSetVerificationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_item_set_verification_status(
        SandboxItemSetVerificationStatusRequest(
            access_token="some example string",
            account_id="some example string",
            verification_status=VerificationStatus1.AUTOMATICALLY_VERIFIED,
        ),
    )
    # TODO: Handle 'response' of type SandboxItemSetVerificationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxItemSetVerificationStatusResponse](the_plaid_api/models/sandbox_item_set_verification_status_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_oauth_select_accounts(body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.sandbox_oauth_select_accounts(
        SandboxOauthSelectAccountsRequest(oauth_state_id="some example string", accounts=["some example string"])
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_oauth_select_accounts(
        SandboxOauthSelectAccountsRequest(oauth_state_id="some example string", accounts=["some example string"])
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_payment_profile_reset_login(body: SandboxPaymentProfileResetLoginRequest | SandboxPaymentProfileResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxPaymentProfileResetLoginResponse</code></summary>

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
try:
    response = client.sandbox_payment_profile_reset_login(
        SandboxPaymentProfileResetLoginRequest(payment_profile_token="some example string")
    )
    # TODO: Handle 'response' of type SandboxPaymentProfileResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_payment_profile_reset_login(
        SandboxPaymentProfileResetLoginRequest(payment_profile_token="some example string")
    )
    # TODO: Handle 'response' of type SandboxPaymentProfileResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxPaymentProfileResetLoginResponse](the_plaid_api/models/sandbox_payment_profile_reset_login_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_payment_simulate(body: SandboxPaymentSimulateRequest | SandboxPaymentSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxPaymentSimulateResponse</code></summary>

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
try:
    response = client.sandbox_payment_simulate(
        SandboxPaymentSimulateRequest(
            payment_id="some example string", webhook="some example string", status="some example string"
        ),
    )
    # TODO: Handle 'response' of type SandboxPaymentSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_payment_simulate(
        SandboxPaymentSimulateRequest(
            payment_id="some example string", webhook="some example string", status="some example string"
        ),
    )
    # TODO: Handle 'response' of type SandboxPaymentSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxPaymentSimulateResponse](the_plaid_api/models/sandbox_payment_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_processor_token_create(body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxProcessorTokenCreateResponse</code></summary>

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
try:
    response = client.sandbox_processor_token_create(
        SandboxProcessorTokenCreateRequest(institution_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_processor_token_create(
        SandboxProcessorTokenCreateRequest(institution_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxProcessorTokenCreateResponse](the_plaid_api/models/sandbox_processor_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_public_token_create(body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxPublicTokenCreateResponse</code></summary>

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
try:
    response = client.sandbox_public_token_create(
        SandboxPublicTokenCreateRequest(institution_id="some example string", initial_products=[Products.ASSETS])
    )
    # TODO: Handle 'response' of type SandboxPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_public_token_create(
        SandboxPublicTokenCreateRequest(institution_id="some example string", initial_products=[Products.ASSETS])
    )
    # TODO: Handle 'response' of type SandboxPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxPublicTokenCreateResponse](the_plaid_api/models/sandbox_public_token_create_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transactions_create(body: SandboxTransactionsCreateRequest | SandboxTransactionsCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransactionsCreateResponse</code></summary>

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
try:
    response = client.sandbox_transactions_create(
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
    # TODO: Handle 'response' of type SandboxTransactionsCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SandboxTransactionsCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.sandbox_transactions_create(
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
    # TODO: Handle 'response' of type SandboxTransactionsCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SandboxTransactionsCreateErrorBody
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

**OnSuccess**: <code>[SandboxTransactionsCreateResponse](the_plaid_api/models/sandbox_transactions_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[SandboxTransactionsCreateErrorBody](the_plaid_api/errors/sandbox_transactions_create_error.py)&#93;</code>

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
<summary><code>def sandbox_transfer_fire_webhook(body: SandboxTransferFireWebhookRequest | SandboxTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferFireWebhookResponse</code></summary>

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
try:
    response = client.sandbox_transfer_fire_webhook(SandboxTransferFireWebhookRequest(webhook="some example string"))
    # TODO: Handle 'response' of type SandboxTransferFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_fire_webhook(
        SandboxTransferFireWebhookRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferFireWebhookResponse](the_plaid_api/models/sandbox_transfer_fire_webhook_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_ledger_deposit_simulate(body: SandboxTransferLedgerDepositSimulateRequest | SandboxTransferLedgerDepositSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferLedgerDepositSimulateResponse</code></summary>

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
try:
    response = client.sandbox_transfer_ledger_deposit_simulate(
        SandboxTransferLedgerDepositSimulateRequest(
            sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
        ),
    )
    # TODO: Handle 'response' of type SandboxTransferLedgerDepositSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_ledger_deposit_simulate(
        SandboxTransferLedgerDepositSimulateRequest(
            sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
        ),
    )
    # TODO: Handle 'response' of type SandboxTransferLedgerDepositSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferLedgerDepositSimulateResponse](the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_ledger_simulate_available(body: SandboxTransferLedgerSimulateAvailableRequest | SandboxTransferLedgerSimulateAvailableRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferLedgerSimulateAvailableResponse</code></summary>

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
try:
    response = client.sandbox_transfer_ledger_simulate_available(SandboxTransferLedgerSimulateAvailableRequest())
    # TODO: Handle 'response' of type SandboxTransferLedgerSimulateAvailableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_ledger_simulate_available(
        SandboxTransferLedgerSimulateAvailableRequest()
    )
    # TODO: Handle 'response' of type SandboxTransferLedgerSimulateAvailableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferLedgerSimulateAvailableResponse](the_plaid_api/models/sandbox_transfer_ledger_simulate_available_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_ledger_withdraw_simulate(body: SandboxTransferLedgerWithdrawSimulateRequest | SandboxTransferLedgerWithdrawSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferLedgerWithdrawSimulateResponse</code></summary>

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
try:
    response = client.sandbox_transfer_ledger_withdraw_simulate(
        SandboxTransferLedgerWithdrawSimulateRequest(
            sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
        ),
    )
    # TODO: Handle 'response' of type SandboxTransferLedgerWithdrawSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_ledger_withdraw_simulate(
        SandboxTransferLedgerWithdrawSimulateRequest(
            sweep_id="some example string", event_type=TransferLedgerSweepSimulateEventType.SWEEP_POSTED
        ),
    )
    # TODO: Handle 'response' of type SandboxTransferLedgerWithdrawSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferLedgerWithdrawSimulateResponse](the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_refund_simulate(body: SandboxTransferRefundSimulateRequest | SandboxTransferRefundSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferRefundSimulateResponse</code></summary>

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
try:
    response = client.sandbox_transfer_refund_simulate(
        SandboxTransferRefundSimulateRequest(refund_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferRefundSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_refund_simulate(
        SandboxTransferRefundSimulateRequest(refund_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferRefundSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferRefundSimulateResponse](the_plaid_api/models/sandbox_transfer_refund_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_repayment_simulate(body: SandboxTransferRepaymentSimulateRequest | SandboxTransferRepaymentSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferRepaymentSimulateResponse</code></summary>

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
try:
    response = client.sandbox_transfer_repayment_simulate(SandboxTransferRepaymentSimulateRequest())
    # TODO: Handle 'response' of type SandboxTransferRepaymentSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_repayment_simulate(SandboxTransferRepaymentSimulateRequest())
    # TODO: Handle 'response' of type SandboxTransferRepaymentSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferRepaymentSimulateResponse](the_plaid_api/models/sandbox_transfer_repayment_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_simulate(body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferSimulateResponse</code></summary>

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
try:
    response = client.sandbox_transfer_simulate(
        SandboxTransferSimulateRequest(transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_simulate(
        SandboxTransferSimulateRequest(transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferSimulateResponse](the_plaid_api/models/sandbox_transfer_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_sweep_simulate(body: SandboxTransferSweepSimulateRequest | SandboxTransferSweepSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferSweepSimulateResponse</code></summary>

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
try:
    response = client.sandbox_transfer_sweep_simulate(SandboxTransferSweepSimulateRequest())
    # TODO: Handle 'response' of type SandboxTransferSweepSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_sweep_simulate(SandboxTransferSweepSimulateRequest())
    # TODO: Handle 'response' of type SandboxTransferSweepSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferSweepSimulateResponse](the_plaid_api/models/sandbox_transfer_sweep_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_advance(body: SandboxTransferTestClockAdvanceRequest | SandboxTransferTestClockAdvanceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferTestClockAdvanceResponse</code></summary>

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
try:
    response = client.sandbox_transfer_test_clock_advance(
        SandboxTransferTestClockAdvanceRequest(
            test_clock_id="some example string", new_virtual_time=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
        ),
    )
    # TODO: Handle 'response' of type SandboxTransferTestClockAdvanceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_test_clock_advance(
        SandboxTransferTestClockAdvanceRequest(
            test_clock_id="some example string", new_virtual_time=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
        ),
    )
    # TODO: Handle 'response' of type SandboxTransferTestClockAdvanceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferTestClockAdvanceResponse](the_plaid_api/models/sandbox_transfer_test_clock_advance_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_create(body: SandboxTransferTestClockCreateRequest | SandboxTransferTestClockCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferTestClockCreateResponse</code></summary>

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
try:
    response = client.sandbox_transfer_test_clock_create(SandboxTransferTestClockCreateRequest())
    # TODO: Handle 'response' of type SandboxTransferTestClockCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_test_clock_create(SandboxTransferTestClockCreateRequest())
    # TODO: Handle 'response' of type SandboxTransferTestClockCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferTestClockCreateResponse](the_plaid_api/models/sandbox_transfer_test_clock_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_get(body: SandboxTransferTestClockGetRequest | SandboxTransferTestClockGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferTestClockGetResponse</code></summary>

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
try:
    response = client.sandbox_transfer_test_clock_get(
        SandboxTransferTestClockGetRequest(test_clock_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferTestClockGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_test_clock_get(
        SandboxTransferTestClockGetRequest(test_clock_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferTestClockGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferTestClockGetResponse](the_plaid_api/models/sandbox_transfer_test_clock_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_test_clock_list(body: SandboxTransferTestClockListRequest | SandboxTransferTestClockListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferTestClockListResponse</code></summary>

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
try:
    response = client.sandbox_transfer_test_clock_list(SandboxTransferTestClockListRequest())
    # TODO: Handle 'response' of type SandboxTransferTestClockListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_transfer_test_clock_list(SandboxTransferTestClockListRequest())
    # TODO: Handle 'response' of type SandboxTransferTestClockListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxTransferTestClockListResponse](the_plaid_api/models/sandbox_transfer_test_clock_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_user_reset_login(body: SandboxUserResetLoginRequest | SandboxUserResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxUserResetLoginResponse</code></summary>

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
try:
    response = client.sandbox_user_reset_login(SandboxUserResetLoginRequest())
    # TODO: Handle 'response' of type SandboxUserResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox_user_reset_login(SandboxUserResetLoginRequest())
    # TODO: Handle 'response' of type SandboxUserResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SandboxUserResetLoginResponse](the_plaid_api/models/sandbox_user_reset_login_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def session_token_create(body: SessionTokenCreateRequest | SessionTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SessionTokenCreateResponse</code></summary>

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
try:
    response = client.session_token_create(SessionTokenCreateRequest(template_id="some example string"))
    # TODO: Handle 'response' of type SessionTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.session_token_create(SessionTokenCreateRequest(template_id="some example string"))
    # TODO: Handle 'response' of type SessionTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SessionTokenCreateResponse](the_plaid_api/models/session_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_decision_report(body: SignalDecisionReportRequest | SignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalDecisionReportResponse</code></summary>

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
try:
    response = client.signal_decision_report(
        SignalDecisionReportRequest(client_transaction_id="some example string", initiated=True)
    )
    # TODO: Handle 'response' of type SignalDecisionReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal_decision_report(
        SignalDecisionReportRequest(client_transaction_id="some example string", initiated=True)
    )
    # TODO: Handle 'response' of type SignalDecisionReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SignalDecisionReportResponse](the_plaid_api/models/signal_decision_report_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_evaluate(body: SignalEvaluateRequest | SignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalEvaluateResponse</code></summary>

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
try:
    response = client.signal_evaluate(
        SignalEvaluateRequest(
            access_token="some example string",
            account_id="some example string",
            client_transaction_id="some example string",
            amount=1.5,
        ),
    )
    # TODO: Handle 'response' of type SignalEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal_evaluate(
        SignalEvaluateRequest(
            access_token="some example string",
            account_id="some example string",
            client_transaction_id="some example string",
            amount=1.5,
        ),
    )
    # TODO: Handle 'response' of type SignalEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SignalEvaluateResponse](the_plaid_api/models/signal_evaluate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_prepare(body: SignalPrepareRequest | SignalPrepareRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalPrepareResponse</code></summary>

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
try:
    response = client.signal_prepare(SignalPrepareRequest(access_token="some example string"))
    # TODO: Handle 'response' of type SignalPrepareResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal_prepare(SignalPrepareRequest(access_token="some example string"))
    # TODO: Handle 'response' of type SignalPrepareResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SignalPrepareResponse](the_plaid_api/models/signal_prepare_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_return_report(body: SignalReturnReportRequest | SignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalReturnReportResponse</code></summary>

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
try:
    response = client.signal_return_report(
        SignalReturnReportRequest(client_transaction_id="some example string", return_code="some example string")
    )
    # TODO: Handle 'response' of type SignalReturnReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal_return_report(
        SignalReturnReportRequest(client_transaction_id="some example string", return_code="some example string")
    )
    # TODO: Handle 'response' of type SignalReturnReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SignalReturnReportResponse](the_plaid_api/models/signal_return_report_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_schedule(body: SignalScheduleRequest | SignalScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalScheduleResponse</code></summary>

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
try:
    response = client.signal_schedule(
        SignalScheduleRequest(
            access_token="some example string",
            account_id="some example string",
            client_transaction_id="some example string",
            amount=1.5,
        ),
    )
    # TODO: Handle 'response' of type SignalScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal_schedule(
        SignalScheduleRequest(
            access_token="some example string",
            account_id="some example string",
            client_transaction_id="some example string",
            amount=1.5,
        ),
    )
    # TODO: Handle 'response' of type SignalScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SignalScheduleResponse](the_plaid_api/models/signal_schedule_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def statements_download(body: StatementsDownloadRequest | StatementsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.statements_download(
        StatementsDownloadRequest(access_token="some example string", statement_id="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.statements_download(
        StatementsDownloadRequest(access_token="some example string", statement_id="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def statements_list(body: StatementsListRequest | StatementsListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> StatementsListResponse</code></summary>

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
try:
    response = client.statements_list(StatementsListRequest(access_token="some example string"))
    # TODO: Handle 'response' of type StatementsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.statements_list(StatementsListRequest(access_token="some example string"))
    # TODO: Handle 'response' of type StatementsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[StatementsListResponse](the_plaid_api/models/statements_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def statements_refresh(body: StatementsRefreshRequest | StatementsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> StatementsRefreshResponse</code></summary>

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
try:
    response = client.statements_refresh(
        StatementsRefreshRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type StatementsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.statements_refresh(
        StatementsRefreshRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type StatementsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[StatementsRefreshResponse](the_plaid_api/models/statements_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_enhance(body: TransactionsEnhanceGetRequest | TransactionsEnhanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsEnhanceGetResponse</code></summary>

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
try:
    response = client.transactions_enhance(
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
    # TODO: Handle 'response' of type TransactionsEnhanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_enhance(
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
    # TODO: Handle 'response' of type TransactionsEnhanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsEnhanceGetResponse](the_plaid_api/models/transactions_enhance_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_enrich(body: TransactionsEnrichRequest | TransactionsEnrichRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsEnrichResponse</code></summary>

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
try:
    response = client.transactions_enrich(
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
    # TODO: Handle 'response' of type TransactionsEnrichResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_enrich(
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
    # TODO: Handle 'response' of type TransactionsEnrichResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsEnrichResponse](the_plaid_api/models/transactions_enrich_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_get(body: TransactionsGetRequest | TransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsGetResponse</code></summary>

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
try:
    response = client.transactions_get(
        TransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type TransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_get(
        TransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type TransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsGetResponse](the_plaid_api/models/transactions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_recurring_get(body: TransactionsRecurringGetRequest | TransactionsRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsRecurringGetResponse</code></summary>

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
try:
    response = client.transactions_recurring_get(TransactionsRecurringGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type TransactionsRecurringGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_recurring_get(
        TransactionsRecurringGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type TransactionsRecurringGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsRecurringGetResponse](the_plaid_api/models/transactions_recurring_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_refresh(body: TransactionsRefreshRequest | TransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsRefreshResponse</code></summary>

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
try:
    response = client.transactions_refresh(TransactionsRefreshRequest(access_token="some example string"))
    # TODO: Handle 'response' of type TransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_refresh(TransactionsRefreshRequest(access_token="some example string"))
    # TODO: Handle 'response' of type TransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsRefreshResponse](the_plaid_api/models/transactions_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_rules_create(body: TransactionsRulesCreateRequest | TransactionsRulesCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsRulesCreateResponse</code></summary>

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
try:
    response = client.transactions_rules_create(
        TransactionsRulesCreateRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            client_user_id="your-client-user-id",
            pfc_primary_category="FOOD_AND_DRINK",
            pfc_detailed_category="FOOD_AND_DRINK_FAST_FOOD",
            rule_details=TransactionsRuleDetails(
                field=TransactionsRuleField.MERCHANT_NAME,
                type_=TransactionsRuleType.SUBSTRING_MATCH,
                query="Burger Shack",
            ),
        ),
    )
    # TODO: Handle 'response' of type TransactionsRulesCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_rules_create(
        TransactionsRulesCreateRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            client_user_id="your-client-user-id",
            pfc_primary_category="FOOD_AND_DRINK",
            pfc_detailed_category="FOOD_AND_DRINK_FAST_FOOD",
            rule_details=TransactionsRuleDetails(
                field=TransactionsRuleField.MERCHANT_NAME,
                type_=TransactionsRuleType.SUBSTRING_MATCH,
                query="Burger Shack",
            ),
        ),
    )
    # TODO: Handle 'response' of type TransactionsRulesCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsRulesCreateResponse](the_plaid_api/models/transactions_rules_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_rules_list(body: TransactionsRulesListRequest | TransactionsRulesListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsRulesListResponse</code></summary>

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
try:
    response = client.transactions_rules_list(
        TransactionsRulesListRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            client_user_id="your-client-user-id",
        ),
    )
    # TODO: Handle 'response' of type TransactionsRulesListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_rules_list(
        TransactionsRulesListRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            client_user_id="your-client-user-id",
        ),
    )
    # TODO: Handle 'response' of type TransactionsRulesListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsRulesListResponse](the_plaid_api/models/transactions_rules_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_rules_remove(body: TransactionsRulesRemoveRequest | TransactionsRulesRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsRulesRemoveResponse</code></summary>

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
try:
    response = client.transactions_rules_remove(
        TransactionsRulesRemoveRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            client_user_id="your-client-user-id",
            rule_id="eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF",
        ),
    )
    # TODO: Handle 'response' of type TransactionsRulesRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_rules_remove(
        TransactionsRulesRemoveRequest(
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
            client_user_id="your-client-user-id",
            rule_id="eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF",
        ),
    )
    # TODO: Handle 'response' of type TransactionsRulesRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsRulesRemoveResponse](the_plaid_api/models/transactions_rules_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_sync(body: TransactionsSyncRequest | TransactionsSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsSyncResponse</code></summary>

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
try:
    response = client.transactions_sync(TransactionsSyncRequest(access_token="some example string"))
    # TODO: Handle 'response' of type TransactionsSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_sync(TransactionsSyncRequest(access_token="some example string"))
    # TODO: Handle 'response' of type TransactionsSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsSyncResponse](the_plaid_api/models/transactions_sync_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_user_insights_get(body: TransactionsUserInsightsGetRequest | TransactionsUserInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsUserInsightsGetResponse</code></summary>

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
try:
    response = client.transactions_user_insights_get(
        TransactionsUserInsightsGetRequest(client_user_id="some example string")
    )
    # TODO: Handle 'response' of type TransactionsUserInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions_user_insights_get(
        TransactionsUserInsightsGetRequest(client_user_id="some example string")
    )
    # TODO: Handle 'response' of type TransactionsUserInsightsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionsUserInsightsGetResponse](the_plaid_api/models/transactions_user_insights_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_authorization_cancel(body: TransferAuthorizationCancelRequest | TransferAuthorizationCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferAuthorizationCancelResponse</code></summary>

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
try:
    response = client.transfer_authorization_cancel(
        TransferAuthorizationCancelRequest(authorization_id="some example string")
    )
    # TODO: Handle 'response' of type TransferAuthorizationCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_authorization_cancel(
        TransferAuthorizationCancelRequest(authorization_id="some example string")
    )
    # TODO: Handle 'response' of type TransferAuthorizationCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferAuthorizationCancelResponse](the_plaid_api/models/transfer_authorization_cancel_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_authorization_create(body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferAuthorizationCreateResponse</code></summary>

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
try:
    response = client.transfer_authorization_create(
        TransferAuthorizationCreateRequest(
            access_token="some example string",
            account_id="some example string",
            type_=TransferType.DEBIT,
            network=TransferNetwork.ACH,
            amount="some example string",
            user=TransferAuthorizationUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferAuthorizationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_authorization_create(
        TransferAuthorizationCreateRequest(
            access_token="some example string",
            account_id="some example string",
            type_=TransferType.DEBIT,
            network=TransferNetwork.ACH,
            amount="some example string",
            user=TransferAuthorizationUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferAuthorizationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferAuthorizationCreateResponse](the_plaid_api/models/transfer_authorization_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_balance_get(body: TransferBalanceGetRequest | TransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferBalanceGetResponse</code></summary>

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
try:
    response = client.transfer_balance_get(TransferBalanceGetRequest())
    # TODO: Handle 'response' of type TransferBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_balance_get(TransferBalanceGetRequest())
    # TODO: Handle 'response' of type TransferBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferBalanceGetResponse](the_plaid_api/models/transfer_balance_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_cancel(body: TransferCancelRequest | TransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferCancelResponse</code></summary>

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
try:
    response = client.transfer_cancel(TransferCancelRequest(transfer_id="some example string"))
    # TODO: Handle 'response' of type TransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_cancel(TransferCancelRequest(transfer_id="some example string"))
    # TODO: Handle 'response' of type TransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferCancelResponse](the_plaid_api/models/transfer_cancel_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_capabilities_get(body: TransferCapabilitiesGetRequest | TransferCapabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferCapabilitiesGetResponse</code></summary>

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
try:
    response = client.transfer_capabilities_get(
        TransferCapabilitiesGetRequest(access_token="some example string", account_id="some example string")
    )
    # TODO: Handle 'response' of type TransferCapabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_capabilities_get(
        TransferCapabilitiesGetRequest(access_token="some example string", account_id="some example string")
    )
    # TODO: Handle 'response' of type TransferCapabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferCapabilitiesGetResponse](the_plaid_api/models/transfer_capabilities_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_configuration_get(body: TransferConfigurationGetRequest | TransferConfigurationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferConfigurationGetResponse</code></summary>

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
try:
    response = client.transfer_configuration_get(TransferConfigurationGetRequest())
    # TODO: Handle 'response' of type TransferConfigurationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_configuration_get(TransferConfigurationGetRequest())
    # TODO: Handle 'response' of type TransferConfigurationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferConfigurationGetResponse](the_plaid_api/models/transfer_configuration_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_create(body: TransferCreateRequest | TransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferCreateResponse</code></summary>

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
try:
    response = client.transfer_create(
        TransferCreateRequest(
            access_token="some example string",
            account_id="some example string",
            authorization_id="some example string",
            description="some example string",
        ),
    )
    # TODO: Handle 'response' of type TransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_create(
        TransferCreateRequest(
            access_token="some example string",
            account_id="some example string",
            authorization_id="some example string",
            description="some example string",
        ),
    )
    # TODO: Handle 'response' of type TransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferCreateResponse](the_plaid_api/models/transfer_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_diligence_document_upload(body: TransferDiligenceDocumentUploadRequest | TransferDiligenceDocumentUploadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferDiligenceDocumentUploadResponse</code></summary>

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
try:
    response = client.transfer_diligence_document_upload(
        TransferDiligenceDocumentUploadRequest(
            originator_client_id="some example string", file=Path("path/to/file.bin"), purpose=Purpose.DUE_DILIGENCE
        ),
    )
    # TODO: Handle 'response' of type TransferDiligenceDocumentUploadResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_diligence_document_upload(
        TransferDiligenceDocumentUploadRequest(
            originator_client_id="some example string", file=Path("path/to/file.bin"), purpose=Purpose.DUE_DILIGENCE
        ),
    )
    # TODO: Handle 'response' of type TransferDiligenceDocumentUploadResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferDiligenceDocumentUploadResponse](the_plaid_api/models/transfer_diligence_document_upload_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_diligence_submit(body: TransferDiligenceSubmitRequest | TransferDiligenceSubmitRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferDiligenceSubmitResponse</code></summary>

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
try:
    response = client.transfer_diligence_submit(
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
    # TODO: Handle 'response' of type TransferDiligenceSubmitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_diligence_submit(
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
    # TODO: Handle 'response' of type TransferDiligenceSubmitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferDiligenceSubmitResponse](the_plaid_api/models/transfer_diligence_submit_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_event_list(body: TransferEventListRequest | TransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferEventListResponse</code></summary>

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
try:
    response = client.transfer_event_list(TransferEventListRequest())
    # TODO: Handle 'response' of type TransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_event_list(TransferEventListRequest())
    # TODO: Handle 'response' of type TransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferEventListResponse](the_plaid_api/models/transfer_event_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_event_sync(body: TransferEventSyncRequest | TransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferEventSyncResponse</code></summary>

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
try:
    response = client.transfer_event_sync(TransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type TransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_event_sync(TransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type TransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferEventSyncResponse](the_plaid_api/models/transfer_event_sync_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_get(body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferGetResponse</code></summary>

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
try:
    response = client.transfer_get(TransferGetRequest())
    # TODO: Handle 'response' of type TransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_get(TransferGetRequest())
    # TODO: Handle 'response' of type TransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferGetResponse](the_plaid_api/models/transfer_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_intent_create(body: TransferIntentCreateRequest | TransferIntentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferIntentCreateResponse</code></summary>

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
try:
    response = client.transfer_intent_create(
        TransferIntentCreateRequest(
            mode=TransferIntentCreateMode.PAYMENT,
            amount="some example string",
            description="some example string",
            user=TransferUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferIntentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_intent_create(
        TransferIntentCreateRequest(
            mode=TransferIntentCreateMode.PAYMENT,
            amount="some example string",
            description="some example string",
            user=TransferUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferIntentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferIntentCreateResponse](the_plaid_api/models/transfer_intent_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_intent_get(body: TransferIntentGetRequest | TransferIntentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferIntentGetResponse</code></summary>

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
try:
    response = client.transfer_intent_get(TransferIntentGetRequest(transfer_intent_id="some example string"))
    # TODO: Handle 'response' of type TransferIntentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_intent_get(
        TransferIntentGetRequest(transfer_intent_id="some example string")
    )
    # TODO: Handle 'response' of type TransferIntentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferIntentGetResponse](the_plaid_api/models/transfer_intent_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_deposit(body: TransferLedgerDepositRequest | TransferLedgerDepositRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferLedgerDepositResponse</code></summary>

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
try:
    response = client.transfer_ledger_deposit(
        TransferLedgerDepositRequest(
            amount="some example string", idempotency_key="some example string", network=TransferAchnetwork.ACH
        ),
    )
    # TODO: Handle 'response' of type TransferLedgerDepositResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_ledger_deposit(
        TransferLedgerDepositRequest(
            amount="some example string", idempotency_key="some example string", network=TransferAchnetwork.ACH
        ),
    )
    # TODO: Handle 'response' of type TransferLedgerDepositResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferLedgerDepositResponse](the_plaid_api/models/transfer_ledger_deposit_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_distribute(body: TransferLedgerDistributeRequest | TransferLedgerDistributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferLedgerDistributeResponse</code></summary>

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
try:
    response = client.transfer_ledger_distribute(
        TransferLedgerDistributeRequest(
            from_ledger_id="some example string",
            to_ledger_id="some example string",
            amount="some example string",
            idempotency_key="some example string",
        ),
    )
    # TODO: Handle 'response' of type TransferLedgerDistributeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_ledger_distribute(
        TransferLedgerDistributeRequest(
            from_ledger_id="some example string",
            to_ledger_id="some example string",
            amount="some example string",
            idempotency_key="some example string",
        ),
    )
    # TODO: Handle 'response' of type TransferLedgerDistributeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferLedgerDistributeResponse](the_plaid_api/models/transfer_ledger_distribute_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_event_list(body: TransferLedgerEventListRequest | TransferLedgerEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferLedgerEventListResponse</code></summary>

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
try:
    response = client.transfer_ledger_event_list(TransferLedgerEventListRequest())
    # TODO: Handle 'response' of type TransferLedgerEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_ledger_event_list(TransferLedgerEventListRequest())
    # TODO: Handle 'response' of type TransferLedgerEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferLedgerEventListResponse](the_plaid_api/models/transfer_ledger_event_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_get(body: TransferLedgerGetRequest | TransferLedgerGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferLedgerGetResponse</code></summary>

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
try:
    response = client.transfer_ledger_get(TransferLedgerGetRequest())
    # TODO: Handle 'response' of type TransferLedgerGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_ledger_get(TransferLedgerGetRequest())
    # TODO: Handle 'response' of type TransferLedgerGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferLedgerGetResponse](the_plaid_api/models/transfer_ledger_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_ledger_withdraw(body: TransferLedgerWithdrawRequest | TransferLedgerWithdrawRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferLedgerWithdrawResponse</code></summary>

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
try:
    response = client.transfer_ledger_withdraw(
        TransferLedgerWithdrawRequest(
            amount="some example string", idempotency_key="some example string", network=TransferNetwork.ACH
        ),
    )
    # TODO: Handle 'response' of type TransferLedgerWithdrawResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_ledger_withdraw(
        TransferLedgerWithdrawRequest(
            amount="some example string", idempotency_key="some example string", network=TransferNetwork.ACH
        ),
    )
    # TODO: Handle 'response' of type TransferLedgerWithdrawResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferLedgerWithdrawResponse](the_plaid_api/models/transfer_ledger_withdraw_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_list(body: TransferListRequest | TransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferListResponse</code></summary>

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
try:
    response = client.transfer_list(TransferListRequest())
    # TODO: Handle 'response' of type TransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_list(TransferListRequest())
    # TODO: Handle 'response' of type TransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferListResponse](the_plaid_api/models/transfer_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_metrics_get(body: TransferMetricsGetRequest | TransferMetricsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferMetricsGetResponse</code></summary>

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
try:
    response = client.transfer_metrics_get(TransferMetricsGetRequest())
    # TODO: Handle 'response' of type TransferMetricsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_metrics_get(TransferMetricsGetRequest())
    # TODO: Handle 'response' of type TransferMetricsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferMetricsGetResponse](the_plaid_api/models/transfer_metrics_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_migrate_account(body: TransferMigrateAccountRequest | TransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferMigrateAccountResponse</code></summary>

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
try:
    response = client.transfer_migrate_account(
        TransferMigrateAccountRequest(
            account_number="some example string",
            routing_number="some example string",
            account_type="some example string",
        ),
    )
    # TODO: Handle 'response' of type TransferMigrateAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_migrate_account(
        TransferMigrateAccountRequest(
            account_number="some example string",
            routing_number="some example string",
            account_type="some example string",
        ),
    )
    # TODO: Handle 'response' of type TransferMigrateAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferMigrateAccountResponse](the_plaid_api/models/transfer_migrate_account_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_create(body: TransferOriginatorCreateRequest | TransferOriginatorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferOriginatorCreateResponse</code></summary>

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
try:
    response = client.transfer_originator_create(TransferOriginatorCreateRequest(company_name="some example string"))
    # TODO: Handle 'response' of type TransferOriginatorCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_originator_create(
        TransferOriginatorCreateRequest(company_name="some example string")
    )
    # TODO: Handle 'response' of type TransferOriginatorCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferOriginatorCreateResponse](the_plaid_api/models/transfer_originator_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_funding_account_create(body: TransferOriginatorFundingAccountCreateRequest | TransferOriginatorFundingAccountCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferOriginatorFundingAccountCreateResponse</code></summary>

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
try:
    response = client.transfer_originator_funding_account_create(
        TransferOriginatorFundingAccountCreateRequest(
            originator_client_id="some example string",
            funding_account=TransferFundingAccountWithDisplayName(
                access_token="some example string", account_id="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type TransferOriginatorFundingAccountCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_originator_funding_account_create(
        TransferOriginatorFundingAccountCreateRequest(
            originator_client_id="some example string",
            funding_account=TransferFundingAccountWithDisplayName(
                access_token="some example string", account_id="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type TransferOriginatorFundingAccountCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferOriginatorFundingAccountCreateResponse](the_plaid_api/models/transfer_originator_funding_account_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_funding_account_update(body: TransferOriginatorFundingAccountUpdateRequest | TransferOriginatorFundingAccountUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferOriginatorFundingAccountUpdateResponse</code></summary>

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
try:
    response = client.transfer_originator_funding_account_update(
        TransferOriginatorFundingAccountUpdateRequest(
            originator_client_id="some example string",
            funding_account=TransferFundingAccount(
                access_token="some example string", account_id="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type TransferOriginatorFundingAccountUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_originator_funding_account_update(
        TransferOriginatorFundingAccountUpdateRequest(
            originator_client_id="some example string",
            funding_account=TransferFundingAccount(
                access_token="some example string", account_id="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type TransferOriginatorFundingAccountUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferOriginatorFundingAccountUpdateResponse](the_plaid_api/models/transfer_originator_funding_account_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_get(body: TransferOriginatorGetRequest | TransferOriginatorGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferOriginatorGetResponse</code></summary>

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
try:
    response = client.transfer_originator_get(TransferOriginatorGetRequest(originator_client_id="some example string"))
    # TODO: Handle 'response' of type TransferOriginatorGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_originator_get(
        TransferOriginatorGetRequest(originator_client_id="some example string")
    )
    # TODO: Handle 'response' of type TransferOriginatorGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferOriginatorGetResponse](the_plaid_api/models/transfer_originator_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_originator_list(body: TransferOriginatorListRequest | TransferOriginatorListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferOriginatorListResponse</code></summary>

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
try:
    response = client.transfer_originator_list(TransferOriginatorListRequest())
    # TODO: Handle 'response' of type TransferOriginatorListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_originator_list(TransferOriginatorListRequest())
    # TODO: Handle 'response' of type TransferOriginatorListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferOriginatorListResponse](the_plaid_api/models/transfer_originator_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_platform_originator_create(body: TransferPlatformOriginatorCreateRequest | TransferPlatformOriginatorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferPlatformOriginatorCreateResponse</code></summary>

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
try:
    response = client.transfer_platform_originator_create(
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
    # TODO: Handle 'response' of type TransferPlatformOriginatorCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_platform_originator_create(
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
    # TODO: Handle 'response' of type TransferPlatformOriginatorCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferPlatformOriginatorCreateResponse](the_plaid_api/models/transfer_platform_originator_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_platform_person_create(body: TransferPlatformPersonCreateRequest | TransferPlatformPersonCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferPlatformPersonCreateResponse</code></summary>

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
try:
    response = client.transfer_platform_person_create(
        TransferPlatformPersonCreateRequest(originator_client_id="some example string")
    )
    # TODO: Handle 'response' of type TransferPlatformPersonCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_platform_person_create(
        TransferPlatformPersonCreateRequest(originator_client_id="some example string")
    )
    # TODO: Handle 'response' of type TransferPlatformPersonCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferPlatformPersonCreateResponse](the_plaid_api/models/transfer_platform_person_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_platform_requirement_submit(body: TransferPlatformRequirementSubmitRequest | TransferPlatformRequirementSubmitRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferPlatformRequirementSubmitResponse</code></summary>

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
try:
    response = client.transfer_platform_requirement_submit(
        TransferPlatformRequirementSubmitRequest(
            originator_client_id="some example string",
            requirement_submissions=[
                RequirementSubmission(requirement_type="some example string", value="some example string")
            ],
        ),
    )
    # TODO: Handle 'response' of type TransferPlatformRequirementSubmitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_platform_requirement_submit(
        TransferPlatformRequirementSubmitRequest(
            originator_client_id="some example string",
            requirement_submissions=[
                RequirementSubmission(requirement_type="some example string", value="some example string")
            ],
        ),
    )
    # TODO: Handle 'response' of type TransferPlatformRequirementSubmitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferPlatformRequirementSubmitResponse](the_plaid_api/models/transfer_platform_requirement_submit_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_questionnaire_create(body: TransferQuestionnaireCreateRequest | TransferQuestionnaireCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferQuestionnaireCreateResponse</code></summary>

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
try:
    response = client.transfer_questionnaire_create(
        TransferQuestionnaireCreateRequest(
            originator_client_id="some example string", redirect_uri="some example string"
        ),
    )
    # TODO: Handle 'response' of type TransferQuestionnaireCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_questionnaire_create(
        TransferQuestionnaireCreateRequest(
            originator_client_id="some example string", redirect_uri="some example string"
        ),
    )
    # TODO: Handle 'response' of type TransferQuestionnaireCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferQuestionnaireCreateResponse](the_plaid_api/models/transfer_questionnaire_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_cancel(body: TransferRecurringCancelRequest | TransferRecurringCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRecurringCancelResponse</code></summary>

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
try:
    response = client.transfer_recurring_cancel(
        TransferRecurringCancelRequest(recurring_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type TransferRecurringCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_recurring_cancel(
        TransferRecurringCancelRequest(recurring_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type TransferRecurringCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRecurringCancelResponse](the_plaid_api/models/transfer_recurring_cancel_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_create(body: TransferRecurringCreateRequest | TransferRecurringCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRecurringCreateResponse</code></summary>

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
try:
    response = client.transfer_recurring_create(
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
    # TODO: Handle 'response' of type TransferRecurringCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_recurring_create(
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
    # TODO: Handle 'response' of type TransferRecurringCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRecurringCreateResponse](the_plaid_api/models/transfer_recurring_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_get(body: TransferRecurringGetRequest | TransferRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRecurringGetResponse</code></summary>

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
try:
    response = client.transfer_recurring_get(TransferRecurringGetRequest(recurring_transfer_id="some example string"))
    # TODO: Handle 'response' of type TransferRecurringGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_recurring_get(
        TransferRecurringGetRequest(recurring_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type TransferRecurringGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRecurringGetResponse](the_plaid_api/models/transfer_recurring_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_recurring_list(body: TransferRecurringListRequest | TransferRecurringListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRecurringListResponse</code></summary>

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
try:
    response = client.transfer_recurring_list(TransferRecurringListRequest())
    # TODO: Handle 'response' of type TransferRecurringListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_recurring_list(TransferRecurringListRequest())
    # TODO: Handle 'response' of type TransferRecurringListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRecurringListResponse](the_plaid_api/models/transfer_recurring_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_refund_cancel(body: TransferRefundCancelRequest | TransferRefundCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRefundCancelResponse</code></summary>

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
try:
    response = client.transfer_refund_cancel(TransferRefundCancelRequest(refund_id="some example string"))
    # TODO: Handle 'response' of type TransferRefundCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_refund_cancel(TransferRefundCancelRequest(refund_id="some example string"))
    # TODO: Handle 'response' of type TransferRefundCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRefundCancelResponse](the_plaid_api/models/transfer_refund_cancel_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_refund_create(body: TransferRefundCreateRequest | TransferRefundCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRefundCreateResponse</code></summary>

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
try:
    response = client.transfer_refund_create(
        TransferRefundCreateRequest(
            transfer_id="some example string", amount="some example string", idempotency_key="some example string"
        ),
    )
    # TODO: Handle 'response' of type TransferRefundCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_refund_create(
        TransferRefundCreateRequest(
            transfer_id="some example string", amount="some example string", idempotency_key="some example string"
        ),
    )
    # TODO: Handle 'response' of type TransferRefundCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRefundCreateResponse](the_plaid_api/models/transfer_refund_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_refund_get(body: TransferRefundGetRequest | TransferRefundGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRefundGetResponse</code></summary>

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
try:
    response = client.transfer_refund_get(TransferRefundGetRequest(refund_id="some example string"))
    # TODO: Handle 'response' of type TransferRefundGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_refund_get(TransferRefundGetRequest(refund_id="some example string"))
    # TODO: Handle 'response' of type TransferRefundGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRefundGetResponse](the_plaid_api/models/transfer_refund_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_repayment_list(body: TransferRepaymentListRequest | TransferRepaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRepaymentListResponse</code></summary>

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
try:
    response = client.transfer_repayment_list(TransferRepaymentListRequest(count=1))
    # TODO: Handle 'response' of type TransferRepaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_repayment_list(TransferRepaymentListRequest(count=1))
    # TODO: Handle 'response' of type TransferRepaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRepaymentListResponse](the_plaid_api/models/transfer_repayment_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_repayment_return_list(body: TransferRepaymentReturnListRequest | TransferRepaymentReturnListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferRepaymentReturnListResponse</code></summary>

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
try:
    response = client.transfer_repayment_return_list(
        TransferRepaymentReturnListRequest(repayment_id="d4bfce70-2470-4298-ae87-5e9b3e18bfaf", count=1)
    )
    # TODO: Handle 'response' of type TransferRepaymentReturnListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_repayment_return_list(
        TransferRepaymentReturnListRequest(repayment_id="d4bfce70-2470-4298-ae87-5e9b3e18bfaf", count=1)
    )
    # TODO: Handle 'response' of type TransferRepaymentReturnListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferRepaymentReturnListResponse](the_plaid_api/models/transfer_repayment_return_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_return_recover(body: TransferReturnRecoverRequest | TransferReturnRecoverRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferReturnRecoverResponse</code></summary>

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
try:
    response = client.transfer_return_recover(
        TransferReturnRecoverRequest(
            transfer_id="some example string", amount="some example string", idempotency_key="some example string"
        ),
    )
    # TODO: Handle 'response' of type TransferReturnRecoverResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_return_recover(
        TransferReturnRecoverRequest(
            transfer_id="some example string", amount="some example string", idempotency_key="some example string"
        ),
    )
    # TODO: Handle 'response' of type TransferReturnRecoverResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferReturnRecoverResponse](the_plaid_api/models/transfer_return_recover_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_sweep_get(body: TransferSweepGetRequest | TransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferSweepGetResponse</code></summary>

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
try:
    response = client.transfer_sweep_get(TransferSweepGetRequest(sweep_id="some example string"))
    # TODO: Handle 'response' of type TransferSweepGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_sweep_get(TransferSweepGetRequest(sweep_id="some example string"))
    # TODO: Handle 'response' of type TransferSweepGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferSweepGetResponse](the_plaid_api/models/transfer_sweep_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_sweep_list(body: TransferSweepListRequest | TransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferSweepListResponse</code></summary>

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
try:
    response = client.transfer_sweep_list(TransferSweepListRequest())
    # TODO: Handle 'response' of type TransferSweepListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_sweep_list(TransferSweepListRequest())
    # TODO: Handle 'response' of type TransferSweepListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransferSweepListResponse](the_plaid_api/models/transfer_sweep_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_account_session_event_send(body: UserAccountSessionEventSendRequest | UserAccountSessionEventSendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserAccountSessionEventSendResponse</code></summary>

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
try:
    response = client.user_account_session_event_send(
        UserAccountSessionEventSendRequest(
            link_session_id="some example string",
            event=UserAccountSessionEvent(
                name="some example string", timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
            ),
        ),
    )
    # TODO: Handle 'response' of type UserAccountSessionEventSendResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_account_session_event_send(
        UserAccountSessionEventSendRequest(
            link_session_id="some example string",
            event=UserAccountSessionEvent(
                name="some example string", timestamp=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)
            ),
        ),
    )
    # TODO: Handle 'response' of type UserAccountSessionEventSendResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserAccountSessionEventSendResponse](the_plaid_api/models/user_account_session_event_send_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_account_session_get(body: UserAccountSessionGetRequest | UserAccountSessionGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserAccountSessionGetResponse</code></summary>

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
try:
    response = client.user_account_session_get(UserAccountSessionGetRequest(public_token="some example string"))
    # TODO: Handle 'response' of type UserAccountSessionGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_account_session_get(
        UserAccountSessionGetRequest(public_token="some example string")
    )
    # TODO: Handle 'response' of type UserAccountSessionGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserAccountSessionGetResponse](the_plaid_api/models/user_account_session_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_create(body: UserCreateRequest | UserCreateRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> UserCreateResponse</code></summary>

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
try:
    response = client.user_create(UserCreateRequest(client_user_id="some example string"))
    # TODO: Handle 'response' of type UserCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_create(UserCreateRequest(client_user_id="some example string"))
    # TODO: Handle 'response' of type UserCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserCreateResponse](the_plaid_api/models/user_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_financial_data_refresh(body: UserFinancialDataRefreshRequest | UserFinancialDataRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserFinancialDataRefreshResponse</code></summary>

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
try:
    response = client.user_financial_data_refresh(UserFinancialDataRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ"))
    # TODO: Handle 'response' of type UserFinancialDataRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_financial_data_refresh(
        UserFinancialDataRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ")
    )
    # TODO: Handle 'response' of type UserFinancialDataRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserFinancialDataRefreshResponse](the_plaid_api/models/user_financial_data_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_get(body: UserGetRequest | UserGetRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> UserGetResponse</code></summary>

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
try:
    response = client.user_get(UserGetRequest(user_id="some example string"))
    # TODO: Handle 'response' of type UserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_get(UserGetRequest(user_id="some example string"))
    # TODO: Handle 'response' of type UserGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserGetResponse](the_plaid_api/models/user_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_identity_remove(body: UserIdentityRemoveRequest | UserIdentityRemoveRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> UserIdentityRemoveResponse</code></summary>

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
try:
    response = client.user_identity_remove(UserIdentityRemoveRequest(user_id="some example string"))
    # TODO: Handle 'response' of type UserIdentityRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_identity_remove(UserIdentityRemoveRequest(user_id="some example string"))
    # TODO: Handle 'response' of type UserIdentityRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserIdentityRemoveResponse](the_plaid_api/models/user_identity_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_items_associate(body: UserItemsAssociateRequest | UserItemsAssociateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserItemsAssociateResponse</code></summary>

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
try:
    response = client.user_items_associate(
        UserItemsAssociateRequest(user_id="some example string", item_ids=["some example string"])
    )
    # TODO: Handle 'response' of type UserItemsAssociateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_items_associate(
        UserItemsAssociateRequest(user_id="some example string", item_ids=["some example string"])
    )
    # TODO: Handle 'response' of type UserItemsAssociateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserItemsAssociateResponse](the_plaid_api/models/user_items_associate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_items_get(body: UserItemsGetRequest | UserItemsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserItemsGetResponse</code></summary>

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
try:
    response = client.user_items_get(UserItemsGetRequest())
    # TODO: Handle 'response' of type UserItemsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_items_get(UserItemsGetRequest())
    # TODO: Handle 'response' of type UserItemsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserItemsGetResponse](the_plaid_api/models/user_items_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_items_remove(body: UserItemsRemoveRequest | UserItemsRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserItemsRemoveResponse</code></summary>

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
try:
    response = client.user_items_remove(UserItemsRemoveRequest(item_ids=["some example string"]))
    # TODO: Handle 'response' of type UserItemsRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_items_remove(UserItemsRemoveRequest(item_ids=["some example string"]))
    # TODO: Handle 'response' of type UserItemsRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserItemsRemoveResponse](the_plaid_api/models/user_items_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_products_terminate(body: UserProductsTerminateRequest | UserProductsTerminateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserProductsTerminateResponse</code></summary>

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
try:
    response = client.user_products_terminate(
        UserProductsTerminateRequest(
            user_id="usr_8c3ZbDBYjaqUXZ",
            reason_code=ProductsTerminateReasonCode.CONSUMER_ACCOUNT_CLOSED,
            reason_note="User closed account with client.",
        ),
    )
    # TODO: Handle 'response' of type UserProductsTerminateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_products_terminate(
        UserProductsTerminateRequest(
            user_id="usr_8c3ZbDBYjaqUXZ",
            reason_code=ProductsTerminateReasonCode.CONSUMER_ACCOUNT_CLOSED,
            reason_note="User closed account with client.",
        ),
    )
    # TODO: Handle 'response' of type UserProductsTerminateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserProductsTerminateResponse](the_plaid_api/models/user_products_terminate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_remove(body: UserRemoveRequest | UserRemoveRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> UserRemoveResponse</code></summary>

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
try:
    response = client.user_remove(UserRemoveRequest())
    # TODO: Handle 'response' of type UserRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_remove(UserRemoveRequest())
    # TODO: Handle 'response' of type UserRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserRemoveResponse](the_plaid_api/models/user_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_third_party_token_create(body: UserThirdPartyTokenCreateRequest | UserThirdPartyTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserThirdPartyTokenCreateResponse</code></summary>

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
try:
    response = client.user_third_party_token_create(
        UserThirdPartyTokenCreateRequest(third_party_client_id="some example string")
    )
    # TODO: Handle 'response' of type UserThirdPartyTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_third_party_token_create(
        UserThirdPartyTokenCreateRequest(third_party_client_id="some example string")
    )
    # TODO: Handle 'response' of type UserThirdPartyTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserThirdPartyTokenCreateResponse](the_plaid_api/models/user_third_party_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_third_party_token_remove(body: UserThirdPartyTokenRemoveRequest | UserThirdPartyTokenRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserThirdPartyTokenRemoveResponse</code></summary>

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
try:
    response = client.user_third_party_token_remove(
        UserThirdPartyTokenRemoveRequest(third_party_user_token="some example string")
    )
    # TODO: Handle 'response' of type UserThirdPartyTokenRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_third_party_token_remove(
        UserThirdPartyTokenRemoveRequest(third_party_user_token="some example string")
    )
    # TODO: Handle 'response' of type UserThirdPartyTokenRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserThirdPartyTokenRemoveResponse](the_plaid_api/models/user_third_party_token_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_transactions_refresh(body: UserTransactionsRefreshRequest | UserTransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserTransactionsRefreshResponse</code></summary>

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
try:
    response = client.user_transactions_refresh(UserTransactionsRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ"))
    # TODO: Handle 'response' of type UserTransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_transactions_refresh(
        UserTransactionsRefreshRequest(user_id="usr_8c3ZbDBYjaqUXZ")
    )
    # TODO: Handle 'response' of type UserTransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserTransactionsRefreshResponse](the_plaid_api/models/user_transactions_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_update(body: UserUpdateRequest | UserUpdateRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> UserUpdateResponse</code></summary>

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
try:
    response = client.user_update(UserUpdateRequest())
    # TODO: Handle 'response' of type UserUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user_update(UserUpdateRequest())
    # TODO: Handle 'response' of type UserUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UserUpdateResponse](the_plaid_api/models/user_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_create(body: WalletCreateRequest | WalletCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WalletCreateResponse</code></summary>

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
try:
    response = client.wallet_create(WalletCreateRequest(iso_currency_code=IsoCurrencyCode.GBP))
    # TODO: Handle 'response' of type WalletCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wallet_create(WalletCreateRequest(iso_currency_code=IsoCurrencyCode.GBP))
    # TODO: Handle 'response' of type WalletCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WalletCreateResponse](the_plaid_api/models/wallet_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_get(body: WalletGetRequest | WalletGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WalletGetResponse</code></summary>

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
try:
    response = client.wallet_get(WalletGetRequest(wallet_id="some example string"))
    # TODO: Handle 'response' of type WalletGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wallet_get(WalletGetRequest(wallet_id="some example string"))
    # TODO: Handle 'response' of type WalletGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WalletGetResponse](the_plaid_api/models/wallet_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_list(body: WalletListRequest | WalletListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WalletListResponse</code></summary>

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
try:
    response = client.wallet_list(WalletListRequest())
    # TODO: Handle 'response' of type WalletListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wallet_list(WalletListRequest())
    # TODO: Handle 'response' of type WalletListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WalletListResponse](the_plaid_api/models/wallet_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_transaction_execute(body: WalletTransactionExecuteRequest | WalletTransactionExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WalletTransactionExecuteResponse</code></summary>

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
try:
    response = client.wallet_transaction_execute(
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
    # TODO: Handle 'response' of type WalletTransactionExecuteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wallet_transaction_execute(
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
    # TODO: Handle 'response' of type WalletTransactionExecuteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WalletTransactionExecuteResponse](the_plaid_api/models/wallet_transaction_execute_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_transaction_get(body: WalletTransactionGetRequest | WalletTransactionGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WalletTransactionGetResponse</code></summary>

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
try:
    response = client.wallet_transaction_get(WalletTransactionGetRequest(transaction_id="some example string"))
    # TODO: Handle 'response' of type WalletTransactionGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wallet_transaction_get(
        WalletTransactionGetRequest(transaction_id="some example string")
    )
    # TODO: Handle 'response' of type WalletTransactionGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WalletTransactionGetResponse](the_plaid_api/models/wallet_transaction_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wallet_transaction_list(body: WalletTransactionListRequest | WalletTransactionListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WalletTransactionListResponse</code></summary>

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
try:
    response = client.wallet_transaction_list(WalletTransactionListRequest(wallet_id="some example string"))
    # TODO: Handle 'response' of type WalletTransactionListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wallet_transaction_list(WalletTransactionListRequest(wallet_id="some example string"))
    # TODO: Handle 'response' of type WalletTransactionListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WalletTransactionListResponse](the_plaid_api/models/wallet_transaction_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_create(body: WatchlistScreeningEntityCreateRequest | WatchlistScreeningEntityCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityCreateResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_create(
        WatchlistScreeningEntityCreateRequest(
            search_terms=EntityWatchlistSearchTerms(
                entity_watchlist_program_id="some example string", legal_name="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_create(
        WatchlistScreeningEntityCreateRequest(
            search_terms=EntityWatchlistSearchTerms(
                entity_watchlist_program_id="some example string", legal_name="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityCreateResponse](the_plaid_api/models/watchlist_screening_entity_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_get(body: WatchlistScreeningEntityGetRequest | WatchlistScreeningEntityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityGetResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_get(
        WatchlistScreeningEntityGetRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_get(
        WatchlistScreeningEntityGetRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityGetResponse](the_plaid_api/models/watchlist_screening_entity_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_history_list(body: WatchlistScreeningEntityHistoryListRequest | WatchlistScreeningEntityHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityHistoryListResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_history_list(
        WatchlistScreeningEntityHistoryListRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityHistoryListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_history_list(
        WatchlistScreeningEntityHistoryListRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityHistoryListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityHistoryListResponse](the_plaid_api/models/watchlist_screening_entity_history_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_hit_list(body: WatchlistScreeningEntityHitListRequest | WatchlistScreeningEntityHitListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityHitListResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_hit_list(
        WatchlistScreeningEntityHitListRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityHitListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_hit_list(
        WatchlistScreeningEntityHitListRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityHitListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityHitListResponse](the_plaid_api/models/watchlist_screening_entity_hit_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_list(body: WatchlistScreeningEntityListRequest | WatchlistScreeningEntityListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityListResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_list(
        WatchlistScreeningEntityListRequest(entity_watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_list(
        WatchlistScreeningEntityListRequest(entity_watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityListResponse](the_plaid_api/models/watchlist_screening_entity_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_program_get(body: WatchlistScreeningEntityProgramGetRequest | WatchlistScreeningEntityProgramGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityProgramGetResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_program_get(
        WatchlistScreeningEntityProgramGetRequest(entity_watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityProgramGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_program_get(
        WatchlistScreeningEntityProgramGetRequest(entity_watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityProgramGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityProgramGetResponse](the_plaid_api/models/watchlist_screening_entity_program_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_program_list(body: WatchlistScreeningEntityProgramListRequest | WatchlistScreeningEntityProgramListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityProgramListResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_program_list(WatchlistScreeningEntityProgramListRequest())
    # TODO: Handle 'response' of type WatchlistScreeningEntityProgramListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_program_list(WatchlistScreeningEntityProgramListRequest())
    # TODO: Handle 'response' of type WatchlistScreeningEntityProgramListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityProgramListResponse](the_plaid_api/models/watchlist_screening_entity_program_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_review_create(body: WatchlistScreeningEntityReviewCreateRequest | WatchlistScreeningEntityReviewCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityReviewCreateResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_review_create(
        WatchlistScreeningEntityReviewCreateRequest(
            confirmed_hits=["some example string"],
            dismissed_hits=["some example string"],
            entity_watchlist_screening_id="some example string",
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityReviewCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_review_create(
        WatchlistScreeningEntityReviewCreateRequest(
            confirmed_hits=["some example string"],
            dismissed_hits=["some example string"],
            entity_watchlist_screening_id="some example string",
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityReviewCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityReviewCreateResponse](the_plaid_api/models/watchlist_screening_entity_review_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_review_list(body: WatchlistScreeningEntityReviewListRequest | WatchlistScreeningEntityReviewListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityReviewListResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_review_list(
        WatchlistScreeningEntityReviewListRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityReviewListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_review_list(
        WatchlistScreeningEntityReviewListRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityReviewListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityReviewListResponse](the_plaid_api/models/watchlist_screening_entity_review_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_entity_update(body: WatchlistScreeningEntityUpdateRequest | WatchlistScreeningEntityUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningEntityUpdateResponse</code></summary>

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
try:
    response = client.watchlist_screening_entity_update(
        WatchlistScreeningEntityUpdateRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_entity_update(
        WatchlistScreeningEntityUpdateRequest(entity_watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningEntityUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningEntityUpdateResponse](the_plaid_api/models/watchlist_screening_entity_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_create(body: WatchlistScreeningIndividualCreateRequest | WatchlistScreeningIndividualCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualCreateResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_create(
        WatchlistScreeningIndividualCreateRequest(
            search_terms=WatchlistScreeningRequestSearchTerms(
                watchlist_program_id="some example string", legal_name="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_create(
        WatchlistScreeningIndividualCreateRequest(
            search_terms=WatchlistScreeningRequestSearchTerms(
                watchlist_program_id="some example string", legal_name="some example string"
            ),
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualCreateResponse](the_plaid_api/models/watchlist_screening_individual_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_get(body: WatchlistScreeningIndividualGetRequest | WatchlistScreeningIndividualGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualGetResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_get(
        WatchlistScreeningIndividualGetRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_get(
        WatchlistScreeningIndividualGetRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualGetResponse](the_plaid_api/models/watchlist_screening_individual_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_history_list(body: WatchlistScreeningIndividualHistoryListRequest | WatchlistScreeningIndividualHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualHistoryListResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_history_list(
        WatchlistScreeningIndividualHistoryListRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualHistoryListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_history_list(
        WatchlistScreeningIndividualHistoryListRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualHistoryListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualHistoryListResponse](the_plaid_api/models/watchlist_screening_individual_history_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_hit_list(body: WatchlistScreeningIndividualHitListRequest | WatchlistScreeningIndividualHitListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualHitListResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_hit_list(
        WatchlistScreeningIndividualHitListRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualHitListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_hit_list(
        WatchlistScreeningIndividualHitListRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualHitListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualHitListResponse](the_plaid_api/models/watchlist_screening_individual_hit_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_list(body: WatchlistScreeningIndividualListRequest | WatchlistScreeningIndividualListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualListResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_list(
        WatchlistScreeningIndividualListRequest(watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_list(
        WatchlistScreeningIndividualListRequest(watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualListResponse](the_plaid_api/models/watchlist_screening_individual_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_program_get(body: WatchlistScreeningIndividualProgramGetRequest | WatchlistScreeningIndividualProgramGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualProgramGetResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_program_get(
        WatchlistScreeningIndividualProgramGetRequest(watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualProgramGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_program_get(
        WatchlistScreeningIndividualProgramGetRequest(watchlist_program_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualProgramGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualProgramGetResponse](the_plaid_api/models/watchlist_screening_individual_program_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_program_list(body: WatchlistScreeningIndividualProgramListRequest | WatchlistScreeningIndividualProgramListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualProgramListResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_program_list(WatchlistScreeningIndividualProgramListRequest())
    # TODO: Handle 'response' of type WatchlistScreeningIndividualProgramListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_program_list(
        WatchlistScreeningIndividualProgramListRequest()
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualProgramListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualProgramListResponse](the_plaid_api/models/watchlist_screening_individual_program_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_review_create(body: WatchlistScreeningIndividualReviewCreateRequest | WatchlistScreeningIndividualReviewCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualReviewCreateResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_review_create(
        WatchlistScreeningIndividualReviewCreateRequest(
            confirmed_hits=["some example string"],
            dismissed_hits=["some example string"],
            watchlist_screening_id="some example string",
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualReviewCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_review_create(
        WatchlistScreeningIndividualReviewCreateRequest(
            confirmed_hits=["some example string"],
            dismissed_hits=["some example string"],
            watchlist_screening_id="some example string",
        ),
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualReviewCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualReviewCreateResponse](the_plaid_api/models/watchlist_screening_individual_review_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_review_list(body: WatchlistScreeningIndividualReviewListRequest | WatchlistScreeningIndividualReviewListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualReviewListResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_review_list(
        WatchlistScreeningIndividualReviewListRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualReviewListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_review_list(
        WatchlistScreeningIndividualReviewListRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualReviewListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualReviewListResponse](the_plaid_api/models/watchlist_screening_individual_review_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def watchlist_screening_individual_update(body: WatchlistScreeningIndividualUpdateRequest | WatchlistScreeningIndividualUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WatchlistScreeningIndividualUpdateResponse</code></summary>

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
try:
    response = client.watchlist_screening_individual_update(
        WatchlistScreeningIndividualUpdateRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.watchlist_screening_individual_update(
        WatchlistScreeningIndividualUpdateRequest(watchlist_screening_id="some example string")
    )
    # TODO: Handle 'response' of type WatchlistScreeningIndividualUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WatchlistScreeningIndividualUpdateResponse](the_plaid_api/models/watchlist_screening_individual_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def webhook_verification_key_get(body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WebhookVerificationKeyGetResponse</code></summary>

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
try:
    response = client.webhook_verification_key_get(WebhookVerificationKeyGetRequest(key_id="some example string"))
    # TODO: Handle 'response' of type WebhookVerificationKeyGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.webhook_verification_key_get(
        WebhookVerificationKeyGetRequest(key_id="some example string")
    )
    # TODO: Handle 'response' of type WebhookVerificationKeyGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WebhookVerificationKeyGetResponse](the_plaid_api/models/webhook_verification_key_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

