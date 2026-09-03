<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `the_plaid_api/client.py` · 335 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.accounts_balance_get

- **Route**: `POST /accounts/balance/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def accounts_balance_get(body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountsGetResponse`
- **Returns (raw)**: `ApiResult[AccountsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountsBalanceGetRequest` | `the_plaid_api/models/accounts_balance_get_request.py` |
| `AccountsBalanceGetRequestDict` | `the_plaid_api/models/accounts_balance_get_request.py` |
| `AccountsGetResponse` | `the_plaid_api/models/accounts_get_response.py` |

### client.accounts_get

- **Route**: `POST /accounts/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def accounts_get(body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountsGetResponse`
- **Returns (raw)**: `ApiResult[AccountsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountsGetRequest` | `the_plaid_api/models/accounts_get_request.py` |
| `AccountsGetRequestDict` | `the_plaid_api/models/accounts_get_request.py` |
| `AccountsGetResponse` | `the_plaid_api/models/accounts_get_response.py` |

### client.application_get

- **Route**: `POST /application/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def application_get(body: ApplicationGetRequest | ApplicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ApplicationGetResponse`
- **Returns (raw)**: `ApiResult[ApplicationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApplicationGetRequest` | `the_plaid_api/models/application_get_request.py` |
| `ApplicationGetRequestDict` | `the_plaid_api/models/application_get_request.py` |
| `ApplicationGetResponse` | `the_plaid_api/models/application_get_response.py` |

### client.asset_report_audit_copy_create

- **Route**: `POST /asset_report/audit_copy/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_audit_copy_create(body: AssetReportAuditCopyCreateRequest | AssetReportAuditCopyCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportAuditCopyCreateResponse`
- **Returns (raw)**: `ApiResult[AssetReportAuditCopyCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportAuditCopyCreateRequest` | `the_plaid_api/models/asset_report_audit_copy_create_request.py` |
| `AssetReportAuditCopyCreateRequestDict` | `the_plaid_api/models/asset_report_audit_copy_create_request.py` |
| `AssetReportAuditCopyCreateResponse` | `the_plaid_api/models/asset_report_audit_copy_create_response.py` |

### client.asset_report_audit_copy_get

- **Route**: `POST /asset_report/audit_copy/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_audit_copy_get(body: AssetReportAuditCopyGetRequest | AssetReportAuditCopyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportGetResponse`
- **Returns (raw)**: `ApiResult[AssetReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportAuditCopyGetRequest` | `the_plaid_api/models/asset_report_audit_copy_get_request.py` |
| `AssetReportAuditCopyGetRequestDict` | `the_plaid_api/models/asset_report_audit_copy_get_request.py` |
| `AssetReportGetResponse` | `the_plaid_api/models/asset_report_get_response.py` |

### client.asset_report_audit_copy_pdf_get

- **Route**: `POST /asset_report/audit_copy/pdf/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_audit_copy_pdf_get(body: AssetReportAuditCopyPdfGetRequest | AssetReportAuditCopyPdfGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportAuditCopyPdfGetRequest` | `the_plaid_api/models/asset_report_audit_copy_pdf_get_request.py` |
| `AssetReportAuditCopyPdfGetRequestDict` | `the_plaid_api/models/asset_report_audit_copy_pdf_get_request.py` |

### client.asset_report_audit_copy_remove

- **Route**: `POST /asset_report/audit_copy/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_audit_copy_remove(body: AssetReportAuditCopyRemoveRequest | AssetReportAuditCopyRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportAuditCopyRemoveResponse`
- **Returns (raw)**: `ApiResult[AssetReportAuditCopyRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportAuditCopyRemoveRequest` | `the_plaid_api/models/asset_report_audit_copy_remove_request.py` |
| `AssetReportAuditCopyRemoveRequestDict` | `the_plaid_api/models/asset_report_audit_copy_remove_request.py` |
| `AssetReportAuditCopyRemoveResponse` | `the_plaid_api/models/asset_report_audit_copy_remove_response.py` |

### client.asset_report_create

- **Route**: `POST /asset_report/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_create(body: AssetReportCreateRequest | AssetReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportCreateResponse`
- **Returns (raw)**: `ApiResult[AssetReportCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportCreateRequest` | `the_plaid_api/models/asset_report_create_request.py` |
| `AssetReportCreateRequestDict` | `the_plaid_api/models/asset_report_create_request.py` |
| `AssetReportCreateResponse` | `the_plaid_api/models/asset_report_create_response.py` |

### client.asset_report_filter

- **Route**: `POST /asset_report/filter`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_filter(body: AssetReportFilterRequest | AssetReportFilterRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportFilterResponse`
- **Returns (raw)**: `ApiResult[AssetReportFilterResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportFilterRequest` | `the_plaid_api/models/asset_report_filter_request.py` |
| `AssetReportFilterRequestDict` | `the_plaid_api/models/asset_report_filter_request.py` |
| `AssetReportFilterResponse` | `the_plaid_api/models/asset_report_filter_response.py` |

### client.asset_report_get

- **Route**: `POST /asset_report/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_get(body: AssetReportGetRequest | AssetReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportGetResponse`
- **Returns (raw)**: `ApiResult[AssetReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportGetRequest` | `the_plaid_api/models/asset_report_get_request.py` |
| `AssetReportGetRequestDict` | `the_plaid_api/models/asset_report_get_request.py` |
| `AssetReportGetResponse` | `the_plaid_api/models/asset_report_get_response.py` |

### client.asset_report_pdf_get

- **Route**: `POST /asset_report/pdf/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_pdf_get(body: AssetReportPdfgetRequest | AssetReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportPdfgetRequest` | `the_plaid_api/models/asset_report_pdfget_request.py` |
| `AssetReportPdfgetRequestDict` | `the_plaid_api/models/asset_report_pdfget_request.py` |

### client.asset_report_refresh

- **Route**: `POST /asset_report/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_refresh(body: AssetReportRefreshRequest | AssetReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportRefreshResponse`
- **Returns (raw)**: `ApiResult[AssetReportRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportRefreshRequest` | `the_plaid_api/models/asset_report_refresh_request.py` |
| `AssetReportRefreshRequestDict` | `the_plaid_api/models/asset_report_refresh_request.py` |
| `AssetReportRefreshResponse` | `the_plaid_api/models/asset_report_refresh_response.py` |

### client.asset_report_remove

- **Route**: `POST /asset_report/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def asset_report_remove(body: AssetReportRemoveRequest | AssetReportRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportRemoveResponse`
- **Returns (raw)**: `ApiResult[AssetReportRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportRemoveRequest` | `the_plaid_api/models/asset_report_remove_request.py` |
| `AssetReportRemoveRequestDict` | `the_plaid_api/models/asset_report_remove_request.py` |
| `AssetReportRemoveResponse` | `the_plaid_api/models/asset_report_remove_response.py` |

### client.auth_get

- **Route**: `POST /auth/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def auth_get(body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthGetResponse`
- **Returns (raw)**: `ApiResult[AuthGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AuthGetRequest` | `the_plaid_api/models/auth_get_request.py` |
| `AuthGetRequestDict` | `the_plaid_api/models/auth_get_request.py` |
| `AuthGetResponse` | `the_plaid_api/models/auth_get_response.py` |

### client.auth_verify

- **Route**: `POST /auth/verify`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def auth_verify(body: AuthVerifyRequest | AuthVerifyRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthVerifyResponse`
- **Returns (raw)**: `ApiResult[AuthVerifyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AuthVerifyRequest` | `the_plaid_api/models/auth_verify_request.py` |
| `AuthVerifyRequestDict` | `the_plaid_api/models/auth_verify_request.py` |
| `AuthVerifyResponse` | `the_plaid_api/models/auth_verify_response.py` |

### client.bank_transfer_balance_get

- **Route**: `POST /bank_transfer/balance/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_balance_get(body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferBalanceGetResponse`
- **Returns (raw)**: `ApiResult[BankTransferBalanceGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferBalanceGetRequest` | `the_plaid_api/models/bank_transfer_balance_get_request.py` |
| `BankTransferBalanceGetRequestDict` | `the_plaid_api/models/bank_transfer_balance_get_request.py` |
| `BankTransferBalanceGetResponse` | `the_plaid_api/models/bank_transfer_balance_get_response.py` |

### client.bank_transfer_cancel

- **Route**: `POST /bank_transfer/cancel`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_cancel(body: BankTransferCancelRequest | BankTransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferCancelResponse`
- **Returns (raw)**: `ApiResult[BankTransferCancelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferCancelRequest` | `the_plaid_api/models/bank_transfer_cancel_request.py` |
| `BankTransferCancelRequestDict` | `the_plaid_api/models/bank_transfer_cancel_request.py` |
| `BankTransferCancelResponse` | `the_plaid_api/models/bank_transfer_cancel_response.py` |

### client.bank_transfer_create

- **Route**: `POST /bank_transfer/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_create(body: BankTransferCreateRequest | BankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferCreateResponse`
- **Returns (raw)**: `ApiResult[BankTransferCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferCreateRequest` | `the_plaid_api/models/bank_transfer_create_request.py` |
| `BankTransferCreateRequestDict` | `the_plaid_api/models/bank_transfer_create_request.py` |
| `BankTransferCreateResponse` | `the_plaid_api/models/bank_transfer_create_response.py` |

### client.bank_transfer_event_list

- **Route**: `POST /bank_transfer/event/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_event_list(body: BankTransferEventListRequest | BankTransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferEventListResponse`
- **Returns (raw)**: `ApiResult[BankTransferEventListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferEventListRequest` | `the_plaid_api/models/bank_transfer_event_list_request.py` |
| `BankTransferEventListRequestDict` | `the_plaid_api/models/bank_transfer_event_list_request.py` |
| `BankTransferEventListResponse` | `the_plaid_api/models/bank_transfer_event_list_response.py` |

### client.bank_transfer_event_sync

- **Route**: `POST /bank_transfer/event/sync`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_event_sync(body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferEventSyncResponse`
- **Returns (raw)**: `ApiResult[BankTransferEventSyncResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferEventSyncRequest` | `the_plaid_api/models/bank_transfer_event_sync_request.py` |
| `BankTransferEventSyncRequestDict` | `the_plaid_api/models/bank_transfer_event_sync_request.py` |
| `BankTransferEventSyncResponse` | `the_plaid_api/models/bank_transfer_event_sync_response.py` |

### client.bank_transfer_get

- **Route**: `POST /bank_transfer/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_get(body: BankTransferGetRequest | BankTransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferGetResponse`
- **Returns (raw)**: `ApiResult[BankTransferGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferGetRequest` | `the_plaid_api/models/bank_transfer_get_request.py` |
| `BankTransferGetRequestDict` | `the_plaid_api/models/bank_transfer_get_request.py` |
| `BankTransferGetResponse` | `the_plaid_api/models/bank_transfer_get_response.py` |

### client.bank_transfer_list

- **Route**: `POST /bank_transfer/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_list(body: BankTransferListRequest | BankTransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferListResponse`
- **Returns (raw)**: `ApiResult[BankTransferListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferListRequest` | `the_plaid_api/models/bank_transfer_list_request.py` |
| `BankTransferListRequestDict` | `the_plaid_api/models/bank_transfer_list_request.py` |
| `BankTransferListResponse` | `the_plaid_api/models/bank_transfer_list_response.py` |

### client.bank_transfer_migrate_account

- **Route**: `POST /bank_transfer/migrate_account`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_migrate_account(body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferMigrateAccountResponse`
- **Returns (raw)**: `ApiResult[BankTransferMigrateAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferMigrateAccountRequest` | `the_plaid_api/models/bank_transfer_migrate_account_request.py` |
| `BankTransferMigrateAccountRequestDict` | `the_plaid_api/models/bank_transfer_migrate_account_request.py` |
| `BankTransferMigrateAccountResponse` | `the_plaid_api/models/bank_transfer_migrate_account_response.py` |

### client.bank_transfer_sweep_get

- **Route**: `POST /bank_transfer/sweep/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_sweep_get(body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferSweepGetResponse`
- **Returns (raw)**: `ApiResult[BankTransferSweepGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferSweepGetRequest` | `the_plaid_api/models/bank_transfer_sweep_get_request.py` |
| `BankTransferSweepGetRequestDict` | `the_plaid_api/models/bank_transfer_sweep_get_request.py` |
| `BankTransferSweepGetResponse` | `the_plaid_api/models/bank_transfer_sweep_get_response.py` |

### client.bank_transfer_sweep_list

- **Route**: `POST /bank_transfer/sweep/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def bank_transfer_sweep_list(body: BankTransferSweepListRequest | BankTransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferSweepListResponse`
- **Returns (raw)**: `ApiResult[BankTransferSweepListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferSweepListRequest` | `the_plaid_api/models/bank_transfer_sweep_list_request.py` |
| `BankTransferSweepListRequestDict` | `the_plaid_api/models/bank_transfer_sweep_list_request.py` |
| `BankTransferSweepListResponse` | `the_plaid_api/models/bank_transfer_sweep_list_response.py` |

### client.beacon_account_risk_evaluate

- **Route**: `POST /beacon/account_risk/v1/evaluate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_account_risk_evaluate(body: BeaconAccountRiskEvaluateRequest | BeaconAccountRiskEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconAccountRiskEvaluateResponse`
- **Returns (raw)**: `ApiResult[BeaconAccountRiskEvaluateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconAccountRiskEvaluateRequest` | `the_plaid_api/models/beacon_account_risk_evaluate_request.py` |
| `BeaconAccountRiskEvaluateRequestDict` | `the_plaid_api/models/beacon_account_risk_evaluate_request.py` |
| `BeaconAccountRiskEvaluateResponse` | `the_plaid_api/models/beacon_account_risk_evaluate_response.py` |

### client.beacon_duplicate_get

- **Route**: `POST /beacon/duplicate/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_duplicate_get(body: BeaconDuplicateGetRequest | BeaconDuplicateGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconDuplicateGetResponse`
- **Returns (raw)**: `ApiResult[BeaconDuplicateGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconDuplicateGetRequest` | `the_plaid_api/models/beacon_duplicate_get_request.py` |
| `BeaconDuplicateGetRequestDict` | `the_plaid_api/models/beacon_duplicate_get_request.py` |
| `BeaconDuplicateGetResponse` | `the_plaid_api/models/beacon_duplicate_get_response.py` |

### client.beacon_report_create

- **Route**: `POST /beacon/report/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_report_create(body: BeaconReportCreateRequest | BeaconReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconReportCreateResponse`
- **Returns (raw)**: `ApiResult[BeaconReportCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconReportCreateRequest` | `the_plaid_api/models/beacon_report_create_request.py` |
| `BeaconReportCreateRequestDict` | `the_plaid_api/models/beacon_report_create_request.py` |
| `BeaconReportCreateResponse` | `the_plaid_api/models/beacon_report_create_response.py` |

### client.beacon_report_get

- **Route**: `POST /beacon/report/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_report_get(body: BeaconReportGetRequest | BeaconReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconReportGetResponse`
- **Returns (raw)**: `ApiResult[BeaconReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconReportGetRequest` | `the_plaid_api/models/beacon_report_get_request.py` |
| `BeaconReportGetRequestDict` | `the_plaid_api/models/beacon_report_get_request.py` |
| `BeaconReportGetResponse` | `the_plaid_api/models/beacon_report_get_response.py` |

### client.beacon_report_list

- **Route**: `POST /beacon/report/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_report_list(body: BeaconReportListRequest | BeaconReportListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconReportListResponse`
- **Returns (raw)**: `ApiResult[BeaconReportListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconReportListRequest` | `the_plaid_api/models/beacon_report_list_request.py` |
| `BeaconReportListRequestDict` | `the_plaid_api/models/beacon_report_list_request.py` |
| `BeaconReportListResponse` | `the_plaid_api/models/beacon_report_list_response.py` |

### client.beacon_report_syndication_get

- **Route**: `POST /beacon/report_syndication/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_report_syndication_get(body: BeaconReportSyndicationGetRequest | BeaconReportSyndicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconReportSyndicationGetResponse`
- **Returns (raw)**: `ApiResult[BeaconReportSyndicationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconReportSyndicationGetRequest` | `the_plaid_api/models/beacon_report_syndication_get_request.py` |
| `BeaconReportSyndicationGetRequestDict` | `the_plaid_api/models/beacon_report_syndication_get_request.py` |
| `BeaconReportSyndicationGetResponse` | `the_plaid_api/models/beacon_report_syndication_get_response.py` |

### client.beacon_report_syndication_list

- **Route**: `POST /beacon/report_syndication/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_report_syndication_list(body: BeaconReportSyndicationListRequest | BeaconReportSyndicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconReportSyndicationListResponse`
- **Returns (raw)**: `ApiResult[BeaconReportSyndicationListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconReportSyndicationListRequest` | `the_plaid_api/models/beacon_report_syndication_list_request.py` |
| `BeaconReportSyndicationListRequestDict` | `the_plaid_api/models/beacon_report_syndication_list_request.py` |
| `BeaconReportSyndicationListResponse` | `the_plaid_api/models/beacon_report_syndication_list_response.py` |

### client.beacon_user_account_insights_get

- **Route**: `POST /beacon/user/account_insights/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_user_account_insights_get(body: BeaconUserAccountInsightsGetRequest | BeaconUserAccountInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconUserAccountInsightsGetResponse`
- **Returns (raw)**: `ApiResult[BeaconUserAccountInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconUserAccountInsightsGetRequest` | `the_plaid_api/models/beacon_user_account_insights_get_request.py` |
| `BeaconUserAccountInsightsGetRequestDict` | `the_plaid_api/models/beacon_user_account_insights_get_request.py` |
| `BeaconUserAccountInsightsGetResponse` | `the_plaid_api/models/beacon_user_account_insights_get_response.py` |

### client.beacon_user_create

- **Route**: `POST /beacon/user/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_user_create(body: BeaconUserCreateRequest | BeaconUserCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconUserCreateResponse`
- **Returns (raw)**: `ApiResult[BeaconUserCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconUserCreateRequest` | `the_plaid_api/models/beacon_user_create_request.py` |
| `BeaconUserCreateRequestDict` | `the_plaid_api/models/beacon_user_create_request.py` |
| `BeaconUserCreateResponse` | `the_plaid_api/models/beacon_user_create_response.py` |

### client.beacon_user_get

- **Route**: `POST /beacon/user/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_user_get(body: BeaconUserGetRequest | BeaconUserGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconUserGetResponse`
- **Returns (raw)**: `ApiResult[BeaconUserGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconUserGetRequest` | `the_plaid_api/models/beacon_user_get_request.py` |
| `BeaconUserGetRequestDict` | `the_plaid_api/models/beacon_user_get_request.py` |
| `BeaconUserGetResponse` | `the_plaid_api/models/beacon_user_get_response.py` |

### client.beacon_user_history_list

- **Route**: `POST /beacon/user/history/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_user_history_list(body: BeaconUserHistoryListRequest | BeaconUserHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconUserHistoryListResponse`
- **Returns (raw)**: `ApiResult[BeaconUserHistoryListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconUserHistoryListRequest` | `the_plaid_api/models/beacon_user_history_list_request.py` |
| `BeaconUserHistoryListRequestDict` | `the_plaid_api/models/beacon_user_history_list_request.py` |
| `BeaconUserHistoryListResponse` | `the_plaid_api/models/beacon_user_history_list_response.py` |

### client.beacon_user_review

- **Route**: `POST /beacon/user/review`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_user_review(body: BeaconUserReviewRequest | BeaconUserReviewRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconUserGetResponse`
- **Returns (raw)**: `ApiResult[BeaconUserGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconUserReviewRequest` | `the_plaid_api/models/beacon_user_review_request.py` |
| `BeaconUserReviewRequestDict` | `the_plaid_api/models/beacon_user_review_request.py` |
| `BeaconUserGetResponse` | `the_plaid_api/models/beacon_user_get_response.py` |

### client.beacon_user_update

- **Route**: `POST /beacon/user/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beacon_user_update(body: BeaconUserUpdateRequest | BeaconUserUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeaconUserUpdateResponse`
- **Returns (raw)**: `ApiResult[BeaconUserUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BeaconUserUpdateRequest` | `the_plaid_api/models/beacon_user_update_request.py` |
| `BeaconUserUpdateRequestDict` | `the_plaid_api/models/beacon_user_update_request.py` |
| `BeaconUserUpdateResponse` | `the_plaid_api/models/beacon_user_update_response.py` |

### client.beta_ewa_report_v1_get

- **Route**: `POST /beta/ewa_report/v1/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beta_ewa_report_v1_get(body: BetaEwaReportV1GetRequest | BetaEwaReportV1GetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BetaEwaReportV1GetResponse`
- **Returns (raw)**: `ApiResult[BetaEwaReportV1GetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BetaEwaReportV1GetRequest` | `the_plaid_api/models/beta_ewa_report_v1_get_request.py` |
| `BetaEwaReportV1GetRequestDict` | `the_plaid_api/models/beta_ewa_report_v1_get_request.py` |
| `BetaEwaReportV1GetResponse` | `the_plaid_api/models/beta_ewa_report_v1_get_response.py` |

### client.beta_partner_customer_v1_create

- **Route**: `POST /beta/partner/customer/v1/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beta_partner_customer_v1_create(body: BetaPartnerCustomerV1CreateRequest | BetaPartnerCustomerV1CreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BetaPartnerCustomerV1CreateResponse`
- **Returns (raw)**: `ApiResult[BetaPartnerCustomerV1CreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BetaPartnerCustomerV1CreateRequest` | `the_plaid_api/models/beta_partner_customer_v1_create_request.py` |
| `BetaPartnerCustomerV1CreateRequestDict` | `the_plaid_api/models/beta_partner_customer_v1_create_request.py` |
| `BetaPartnerCustomerV1CreateResponse` | `the_plaid_api/models/beta_partner_customer_v1_create_response.py` |

### client.beta_partner_customer_v1_enable

- **Route**: `POST /beta/partner/customer/v1/enable`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beta_partner_customer_v1_enable(body: BetaPartnerCustomerV1EnableRequest | BetaPartnerCustomerV1EnableRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BetaPartnerCustomerV1EnableResponse`
- **Returns (raw)**: `ApiResult[BetaPartnerCustomerV1EnableResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BetaPartnerCustomerV1EnableRequest` | `the_plaid_api/models/beta_partner_customer_v1_enable_request.py` |
| `BetaPartnerCustomerV1EnableRequestDict` | `the_plaid_api/models/beta_partner_customer_v1_enable_request.py` |
| `BetaPartnerCustomerV1EnableResponse` | `the_plaid_api/models/beta_partner_customer_v1_enable_response.py` |

### client.beta_partner_customer_v1_get

- **Route**: `POST /beta/partner/customer/v1/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beta_partner_customer_v1_get(body: BetaPartnerCustomerV1GetRequest | BetaPartnerCustomerV1GetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BetaPartnerCustomerV1GetResponse`
- **Returns (raw)**: `ApiResult[BetaPartnerCustomerV1GetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BetaPartnerCustomerV1GetRequest` | `the_plaid_api/models/beta_partner_customer_v1_get_request.py` |
| `BetaPartnerCustomerV1GetRequestDict` | `the_plaid_api/models/beta_partner_customer_v1_get_request.py` |
| `BetaPartnerCustomerV1GetResponse` | `the_plaid_api/models/beta_partner_customer_v1_get_response.py` |

### client.beta_partner_customer_v1_update

- **Route**: `POST /beta/partner/customer/v1/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def beta_partner_customer_v1_update(body: BetaPartnerCustomerV1UpdateRequest | BetaPartnerCustomerV1UpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BetaPartnerCustomerV1UpdateResponse`
- **Returns (raw)**: `ApiResult[BetaPartnerCustomerV1UpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BetaPartnerCustomerV1UpdateRequest` | `the_plaid_api/models/beta_partner_customer_v1_update_request.py` |
| `BetaPartnerCustomerV1UpdateRequestDict` | `the_plaid_api/models/beta_partner_customer_v1_update_request.py` |
| `BetaPartnerCustomerV1UpdateResponse` | `the_plaid_api/models/beta_partner_customer_v1_update_response.py` |

### client.business_verification_create

- **Route**: `POST /business_verification/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def business_verification_create(body: BusinessVerificationCreateRequest | BusinessVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BusinessVerificationCreateResponse`
- **Returns (raw)**: `ApiResult[BusinessVerificationCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BusinessVerificationCreateRequest` | `the_plaid_api/models/business_verification_create_request.py` |
| `BusinessVerificationCreateRequestDict` | `the_plaid_api/models/business_verification_create_request.py` |
| `BusinessVerificationCreateResponse` | `the_plaid_api/models/business_verification_create_response.py` |

### client.business_verification_get

- **Route**: `POST /business_verification/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def business_verification_get(body: BusinessVerificationGetRequest | BusinessVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BusinessVerificationGetResponse`
- **Returns (raw)**: `ApiResult[BusinessVerificationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BusinessVerificationGetRequest` | `the_plaid_api/models/business_verification_get_request.py` |
| `BusinessVerificationGetRequestDict` | `the_plaid_api/models/business_verification_get_request.py` |
| `BusinessVerificationGetResponse` | `the_plaid_api/models/business_verification_get_response.py` |

### client.cashflow_report_get

- **Route**: `POST /cashflow_report/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cashflow_report_get(body: CashflowReportGetRequest | CashflowReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CashflowReportGetResponse`
- **Returns (raw)**: `ApiResult[CashflowReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CashflowReportGetRequest` | `the_plaid_api/models/cashflow_report_get_request.py` |
| `CashflowReportGetRequestDict` | `the_plaid_api/models/cashflow_report_get_request.py` |
| `CashflowReportGetResponse` | `the_plaid_api/models/cashflow_report_get_response.py` |

### client.cashflow_report_insights_get

- **Route**: `POST /cashflow_report/insights/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cashflow_report_insights_get(body: CashflowReportInsightsGetRequest | CashflowReportInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CashflowReportInsightsGetResponse`
- **Returns (raw)**: `ApiResult[CashflowReportInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CashflowReportInsightsGetRequest` | `the_plaid_api/models/cashflow_report_insights_get_request.py` |
| `CashflowReportInsightsGetRequestDict` | `the_plaid_api/models/cashflow_report_insights_get_request.py` |
| `CashflowReportInsightsGetResponse` | `the_plaid_api/models/cashflow_report_insights_get_response.py` |

### client.cashflow_report_refresh

- **Route**: `POST /cashflow_report/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cashflow_report_refresh(body: CashflowReportRefreshRequest | CashflowReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CashflowReportRefreshResponse`
- **Returns (raw)**: `ApiResult[CashflowReportRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CashflowReportRefreshRequest` | `the_plaid_api/models/cashflow_report_refresh_request.py` |
| `CashflowReportRefreshRequestDict` | `the_plaid_api/models/cashflow_report_refresh_request.py` |
| `CashflowReportRefreshResponse` | `the_plaid_api/models/cashflow_report_refresh_response.py` |

### client.cashflow_report_transactions_get

- **Route**: `POST /cashflow_report/transactions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cashflow_report_transactions_get(body: CashflowReportTransactionsGetRequest | CashflowReportTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CashflowReportTransactionsGetResponse`
- **Returns (raw)**: `ApiResult[CashflowReportTransactionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CashflowReportTransactionsGetRequest` | `the_plaid_api/models/cashflow_report_transactions_get_request.py` |
| `CashflowReportTransactionsGetRequestDict` | `the_plaid_api/models/cashflow_report_transactions_get_request.py` |
| `CashflowReportTransactionsGetResponse` | `the_plaid_api/models/cashflow_report_transactions_get_response.py` |

### client.categories_get

- **Route**: `POST /categories/get`
- **Server**: `default`
- **Signature**: `def categories_get(body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CategoriesGetResponse`
- **Returns (raw)**: `ApiResult[CategoriesGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CategoriesGetResponse` | `the_plaid_api/models/categories_get_response.py` |

### client.consent_events_get

- **Route**: `POST /consent/events/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def consent_events_get(body: ConsentEventsGetRequest | ConsentEventsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ConsentEventsGetResponse`
- **Returns (raw)**: `ApiResult[ConsentEventsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConsentEventsGetRequest` | `the_plaid_api/models/consent_events_get_request.py` |
| `ConsentEventsGetRequestDict` | `the_plaid_api/models/consent_events_get_request.py` |
| `ConsentEventsGetResponse` | `the_plaid_api/models/consent_events_get_response.py` |

### client.consumer_report_pdf_get

- **Route**: `POST /consumer_report/pdf/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def consumer_report_pdf_get(body: ConsumerReportPdfgetRequest | ConsumerReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConsumerReportPdfgetRequest` | `the_plaid_api/models/consumer_report_pdfget_request.py` |
| `ConsumerReportPdfgetRequestDict` | `the_plaid_api/models/consumer_report_pdfget_request.py` |

### client.cra_check_report_base_report_get

- **Route**: `POST /cra/check_report/base_report/get`
- **Auth**: (`client_id` AND `secret` AND `plaid_version`) OR `oauth2`
- **Server**: `default`
- **Signature**: `def cra_check_report_base_report_get(body: CraCheckReportBaseReportGetRequest | CraCheckReportBaseReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportBaseReportGetResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportBaseReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportBaseReportGetRequest` | `the_plaid_api/models/cra_check_report_base_report_get_request.py` |
| `CraCheckReportBaseReportGetRequestDict` | `the_plaid_api/models/cra_check_report_base_report_get_request.py` |
| `CraCheckReportBaseReportGetResponse` | `the_plaid_api/models/cra_check_report_base_report_get_response.py` |

### client.cra_check_report_cashflow_insights_get

- **Route**: `POST /cra/check_report/cashflow_insights/get`
- **Auth**: (`client_id` AND `secret` AND `plaid_version`) OR `oauth2`
- **Server**: `default`
- **Signature**: `def cra_check_report_cashflow_insights_get(body: CraCheckReportCashflowInsightsGetRequest | CraCheckReportCashflowInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportCashflowInsightsGetResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportCashflowInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportCashflowInsightsGetRequest` | `the_plaid_api/models/cra_check_report_cashflow_insights_get_request.py` |
| `CraCheckReportCashflowInsightsGetRequestDict` | `the_plaid_api/models/cra_check_report_cashflow_insights_get_request.py` |
| `CraCheckReportCashflowInsightsGetResponse` | `the_plaid_api/models/cra_check_report_cashflow_insights_get_response.py` |

### client.cra_check_report_create

- **Route**: `POST /cra/check_report/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_check_report_create(body: CraCheckReportCreateRequest | CraCheckReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportCreateResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportCreateRequest` | `the_plaid_api/models/cra_check_report_create_request.py` |
| `CraCheckReportCreateRequestDict` | `the_plaid_api/models/cra_check_report_create_request.py` |
| `CraCheckReportCreateResponse` | `the_plaid_api/models/cra_check_report_create_response.py` |

### client.cra_check_report_income_insights_get

- **Route**: `POST /cra/check_report/income_insights/get`
- **Auth**: (`client_id` AND `secret` AND `plaid_version`) OR `oauth2`
- **Server**: `default`
- **Signature**: `def cra_check_report_income_insights_get(body: CraCheckReportIncomeInsightsGetRequest | CraCheckReportIncomeInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportIncomeInsightsGetResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportIncomeInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportIncomeInsightsGetRequest` | `the_plaid_api/models/cra_check_report_income_insights_get_request.py` |
| `CraCheckReportIncomeInsightsGetRequestDict` | `the_plaid_api/models/cra_check_report_income_insights_get_request.py` |
| `CraCheckReportIncomeInsightsGetResponse` | `the_plaid_api/models/cra_check_report_income_insights_get_response.py` |

### client.cra_check_report_lend_score_get

- **Route**: `POST /cra/check_report/lend_score/get`
- **Auth**: (`client_id` AND `secret` AND `plaid_version`) OR `oauth2`
- **Server**: `default`
- **Signature**: `def cra_check_report_lend_score_get(body: CraCheckReportLendScoreGetRequest | CraCheckReportLendScoreGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportLendScoreGetResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportLendScoreGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportLendScoreGetRequest` | `the_plaid_api/models/cra_check_report_lend_score_get_request.py` |
| `CraCheckReportLendScoreGetRequestDict` | `the_plaid_api/models/cra_check_report_lend_score_get_request.py` |
| `CraCheckReportLendScoreGetResponse` | `the_plaid_api/models/cra_check_report_lend_score_get_response.py` |

### client.cra_check_report_network_insights_get

- **Route**: `POST /cra/check_report/network_insights/get`
- **Auth**: (`client_id` AND `secret` AND `plaid_version`) OR `oauth2`
- **Server**: `default`
- **Signature**: `def cra_check_report_network_insights_get(body: CraCheckReportNetworkInsightsGetRequest | CraCheckReportNetworkInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportNetworkInsightsGetResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportNetworkInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportNetworkInsightsGetRequest` | `the_plaid_api/models/cra_check_report_network_insights_get_request.py` |
| `CraCheckReportNetworkInsightsGetRequestDict` | `the_plaid_api/models/cra_check_report_network_insights_get_request.py` |
| `CraCheckReportNetworkInsightsGetResponse` | `the_plaid_api/models/cra_check_report_network_insights_get_response.py` |

### client.cra_check_report_partner_insights_get

- **Route**: `POST /cra/check_report/partner_insights/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_check_report_partner_insights_get(body: CraCheckReportPartnerInsightsGetRequest | CraCheckReportPartnerInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportPartnerInsightsGetResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportPartnerInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportPartnerInsightsGetRequest` | `the_plaid_api/models/cra_check_report_partner_insights_get_request.py` |
| `CraCheckReportPartnerInsightsGetRequestDict` | `the_plaid_api/models/cra_check_report_partner_insights_get_request.py` |
| `CraCheckReportPartnerInsightsGetResponse` | `the_plaid_api/models/cra_check_report_partner_insights_get_response.py` |

### client.cra_check_report_pdf_get

- **Route**: `POST /cra/check_report/pdf/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_check_report_pdf_get(body: CraCheckReportPdfgetRequest | CraCheckReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportPdfgetRequest` | `the_plaid_api/models/cra_check_report_pdfget_request.py` |
| `CraCheckReportPdfgetRequestDict` | `the_plaid_api/models/cra_check_report_pdfget_request.py` |

### client.cra_check_report_verification_get

- **Route**: `POST /cra/check_report/verification/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_check_report_verification_get(body: CraCheckReportVerificationGetRequest | CraCheckReportVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCheckReportVerificationGetResponse`
- **Returns (raw)**: `ApiResult[CraCheckReportVerificationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportVerificationGetRequest` | `the_plaid_api/models/cra_check_report_verification_get_request.py` |
| `CraCheckReportVerificationGetRequestDict` | `the_plaid_api/models/cra_check_report_verification_get_request.py` |
| `CraCheckReportVerificationGetResponse` | `the_plaid_api/models/cra_check_report_verification_get_response.py` |

### client.cra_check_report_verification_pdf_get

- **Route**: `POST /cra/check_report/verification/pdf/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_check_report_verification_pdf_get(body: CraCheckReportVerificationPdfGetRequest | CraCheckReportVerificationPdfGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCheckReportVerificationPdfGetRequest` | `the_plaid_api/models/cra_check_report_verification_pdf_get_request.py` |
| `CraCheckReportVerificationPdfGetRequestDict` | `the_plaid_api/models/cra_check_report_verification_pdf_get_request.py` |

### client.cra_credit_profile_report_get

- **Route**: `POST /cra/credit_profile/report/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_credit_profile_report_get(body: CraCreditProfileReportGetRequest | CraCreditProfileReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraCreditProfileReportGetResponse`
- **Returns (raw)**: `ApiResult[CraCreditProfileReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraCreditProfileReportGetRequest` | `the_plaid_api/models/cra_credit_profile_report_get_request.py` |
| `CraCreditProfileReportGetRequestDict` | `the_plaid_api/models/cra_credit_profile_report_get_request.py` |
| `CraCreditProfileReportGetResponse` | `the_plaid_api/models/cra_credit_profile_report_get_response.py` |

### client.cra_loans_applications_register

- **Route**: `POST /cra/loans/applications/register`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_loans_applications_register(body: CraLoansApplicationsRegisterRequest | CraLoansApplicationsRegisterRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraLoansApplicationsRegisterResponse`
- **Returns (raw)**: `ApiResult[CraLoansApplicationsRegisterResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraLoansApplicationsRegisterRequest` | `the_plaid_api/models/cra_loans_applications_register_request.py` |
| `CraLoansApplicationsRegisterRequestDict` | `the_plaid_api/models/cra_loans_applications_register_request.py` |
| `CraLoansApplicationsRegisterResponse` | `the_plaid_api/models/cra_loans_applications_register_response.py` |

### client.cra_loans_register

- **Route**: `POST /cra/loans/register`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_loans_register(body: CraloansRegisterRequest | CraloansRegisterRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraLoansRegisterResponse`
- **Returns (raw)**: `ApiResult[CraLoansRegisterResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraloansRegisterRequest` | `the_plaid_api/models/craloans_register_request.py` |
| `CraloansRegisterRequestDict` | `the_plaid_api/models/craloans_register_request.py` |
| `CraLoansRegisterResponse` | `the_plaid_api/models/cra_loans_register_response.py` |

### client.cra_loans_unregister

- **Route**: `POST /cra/loans/unregister`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_loans_unregister(body: CraLoansUnregisterRequest | CraLoansUnregisterRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraLoanUnregisterResponse`
- **Returns (raw)**: `ApiResult[CraLoanUnregisterResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraLoansUnregisterRequest` | `the_plaid_api/models/cra_loans_unregister_request.py` |
| `CraLoansUnregisterRequestDict` | `the_plaid_api/models/cra_loans_unregister_request.py` |
| `CraLoanUnregisterResponse` | `the_plaid_api/models/cra_loan_unregister_response.py` |

### client.cra_loans_update

- **Route**: `POST /cra/loans/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_loans_update(body: CraLoansUpdateRequest | CraLoansUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraLoansUpdateResponse`
- **Returns (raw)**: `ApiResult[CraLoansUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraLoansUpdateRequest` | `the_plaid_api/models/cra_loans_update_request.py` |
| `CraLoansUpdateRequestDict` | `the_plaid_api/models/cra_loans_update_request.py` |
| `CraLoansUpdateResponse` | `the_plaid_api/models/cra_loans_update_response.py` |

### client.cra_monitoring_insights_get

- **Route**: `POST /cra/monitoring_insights/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_monitoring_insights_get(body: CraMonitoringInsightsGetRequest | CraMonitoringInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraMonitoringInsightsGetResponse`
- **Returns (raw)**: `ApiResult[CraMonitoringInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraMonitoringInsightsGetRequest` | `the_plaid_api/models/cra_monitoring_insights_get_request.py` |
| `CraMonitoringInsightsGetRequestDict` | `the_plaid_api/models/cra_monitoring_insights_get_request.py` |
| `CraMonitoringInsightsGetResponse` | `the_plaid_api/models/cra_monitoring_insights_get_response.py` |

### client.cra_monitoring_insights_subscribe

- **Route**: `POST /cra/monitoring_insights/subscribe`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_monitoring_insights_subscribe(body: CraMonitoringInsightsSubscribeRequest | CraMonitoringInsightsSubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraMonitoringInsightsSubscribeResponse`
- **Returns (raw)**: `ApiResult[CraMonitoringInsightsSubscribeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraMonitoringInsightsSubscribeRequest` | `the_plaid_api/models/cra_monitoring_insights_subscribe_request.py` |
| `CraMonitoringInsightsSubscribeRequestDict` | `the_plaid_api/models/cra_monitoring_insights_subscribe_request.py` |
| `CraMonitoringInsightsSubscribeResponse` | `the_plaid_api/models/cra_monitoring_insights_subscribe_response.py` |

### client.cra_monitoring_insights_unsubscribe

- **Route**: `POST /cra/monitoring_insights/unsubscribe`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_monitoring_insights_unsubscribe(body: CraMonitoringInsightsUnsubscribeRequest | CraMonitoringInsightsUnsubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraMonitoringInsightsUnsubscribeResponse`
- **Returns (raw)**: `ApiResult[CraMonitoringInsightsUnsubscribeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraMonitoringInsightsUnsubscribeRequest` | `the_plaid_api/models/cra_monitoring_insights_unsubscribe_request.py` |
| `CraMonitoringInsightsUnsubscribeRequestDict` | `the_plaid_api/models/cra_monitoring_insights_unsubscribe_request.py` |
| `CraMonitoringInsightsUnsubscribeResponse` | `the_plaid_api/models/cra_monitoring_insights_unsubscribe_response.py` |

### client.cra_partner_insights_get

- **Route**: `POST /cra/partner_insights/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_partner_insights_get(body: CraPartnerInsightsGetRequest | CraPartnerInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraPartnerInsightsGetResponse`
- **Returns (raw)**: `ApiResult[CraPartnerInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraPartnerInsightsGetRequest` | `the_plaid_api/models/cra_partner_insights_get_request.py` |
| `CraPartnerInsightsGetRequestDict` | `the_plaid_api/models/cra_partner_insights_get_request.py` |
| `CraPartnerInsightsGetResponse` | `the_plaid_api/models/cra_partner_insights_get_response.py` |

### client.cra_report_get

- **Route**: `POST /cra/report/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def cra_report_get(body: CraReportGetRequest | CraReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CraReportGetResponse`
- **Returns (raw)**: `ApiResult[CraReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CraReportGetRequest` | `the_plaid_api/models/cra_report_get_request.py` |
| `CraReportGetRequestDict` | `the_plaid_api/models/cra_report_get_request.py` |
| `CraReportGetResponse` | `the_plaid_api/models/cra_report_get_response.py` |

### client.create_payment_token

- **Route**: `POST /payment_initiation/payment/token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def create_payment_token(body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentTokenCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentTokenCreateRequest` | `the_plaid_api/models/payment_initiation_payment_token_create_request.py` |
| `PaymentInitiationPaymentTokenCreateRequestDict` | `the_plaid_api/models/payment_initiation_payment_token_create_request.py` |
| `PaymentInitiationPaymentTokenCreateResponse` | `the_plaid_api/models/payment_initiation_payment_token_create_response.py` |

### client.credit_asset_report_freddie_mac_get

- **Route**: `POST /credit/asset_report/freddie_mac/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_asset_report_freddie_mac_get(body: AssetReportFreddieGetRequest | AssetReportFreddieGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportFreddieGetResponse`
- **Returns (raw)**: `ApiResult[AssetReportFreddieGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportFreddieGetRequest` | `the_plaid_api/models/asset_report_freddie_get_request.py` |
| `AssetReportFreddieGetRequestDict` | `the_plaid_api/models/asset_report_freddie_get_request.py` |
| `AssetReportFreddieGetResponse` | `the_plaid_api/models/asset_report_freddie_get_response.py` |

### client.credit_audit_copy_token_create

- **Route**: `POST /credit/audit_copy_token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_audit_copy_token_create(body: CreditAuditCopyTokenCreateRequest | CreditAuditCopyTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditAuditCopyTokenCreateResponse`
- **Returns (raw)**: `ApiResult[CreditAuditCopyTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditAuditCopyTokenCreateRequest` | `the_plaid_api/models/credit_audit_copy_token_create_request.py` |
| `CreditAuditCopyTokenCreateRequestDict` | `the_plaid_api/models/credit_audit_copy_token_create_request.py` |
| `CreditAuditCopyTokenCreateResponse` | `the_plaid_api/models/credit_audit_copy_token_create_response.py` |

### client.credit_audit_copy_token_update

- **Route**: `POST /credit/audit_copy_token/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_audit_copy_token_update(body: CreditAuditCopyTokenUpdateRequest | CreditAuditCopyTokenUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditAuditCopyTokenUpdateResponse`
- **Returns (raw)**: `ApiResult[CreditAuditCopyTokenUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditAuditCopyTokenUpdateRequest` | `the_plaid_api/models/credit_audit_copy_token_update_request.py` |
| `CreditAuditCopyTokenUpdateRequestDict` | `the_plaid_api/models/credit_audit_copy_token_update_request.py` |
| `CreditAuditCopyTokenUpdateResponse` | `the_plaid_api/models/credit_audit_copy_token_update_response.py` |

### client.credit_bank_employment_get

- **Route**: `POST /beta/credit/v1/bank_employment/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_bank_employment_get(body: CreditBankEmploymentGetRequest | CreditBankEmploymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditBankEmploymentGetResponse`
- **Returns (raw)**: `ApiResult[CreditBankEmploymentGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditBankEmploymentGetRequest` | `the_plaid_api/models/credit_bank_employment_get_request.py` |
| `CreditBankEmploymentGetRequestDict` | `the_plaid_api/models/credit_bank_employment_get_request.py` |
| `CreditBankEmploymentGetResponse` | `the_plaid_api/models/credit_bank_employment_get_response.py` |

### client.credit_bank_income_get

- **Route**: `POST /credit/bank_income/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_bank_income_get(body: CreditBankIncomeGetRequest | CreditBankIncomeGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditBankIncomeGetResponse`
- **Returns (raw)**: `ApiResult[CreditBankIncomeGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditBankIncomeGetRequest` | `the_plaid_api/models/credit_bank_income_get_request.py` |
| `CreditBankIncomeGetRequestDict` | `the_plaid_api/models/credit_bank_income_get_request.py` |
| `CreditBankIncomeGetResponse` | `the_plaid_api/models/credit_bank_income_get_response.py` |

### client.credit_bank_income_pdf_get

- **Route**: `POST /credit/bank_income/pdf/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_bank_income_pdf_get(body: CreditBankIncomePdfgetRequest | CreditBankIncomePdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditBankIncomePdfgetRequest` | `the_plaid_api/models/credit_bank_income_pdfget_request.py` |
| `CreditBankIncomePdfgetRequestDict` | `the_plaid_api/models/credit_bank_income_pdfget_request.py` |

### client.credit_bank_income_refresh

- **Route**: `POST /credit/bank_income/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_bank_income_refresh(body: CreditBankIncomeRefreshRequest | CreditBankIncomeRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditBankIncomeRefreshResponse`
- **Returns (raw)**: `ApiResult[CreditBankIncomeRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditBankIncomeRefreshRequest` | `the_plaid_api/models/credit_bank_income_refresh_request.py` |
| `CreditBankIncomeRefreshRequestDict` | `the_plaid_api/models/credit_bank_income_refresh_request.py` |
| `CreditBankIncomeRefreshResponse` | `the_plaid_api/models/credit_bank_income_refresh_response.py` |

### client.credit_bank_income_webhook_update

- **Route**: `POST /credit/bank_income/webhook/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_bank_income_webhook_update(body: CreditBankIncomeWebhookUpdateRequest | CreditBankIncomeWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditBankIncomeWebhookUpdateResponse`
- **Returns (raw)**: `ApiResult[CreditBankIncomeWebhookUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditBankIncomeWebhookUpdateRequest` | `the_plaid_api/models/credit_bank_income_webhook_update_request.py` |
| `CreditBankIncomeWebhookUpdateRequestDict` | `the_plaid_api/models/credit_bank_income_webhook_update_request.py` |
| `CreditBankIncomeWebhookUpdateResponse` | `the_plaid_api/models/credit_bank_income_webhook_update_response.py` |

### client.credit_bank_statements_uploads_get

- **Route**: `POST /credit/bank_statements/uploads/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_bank_statements_uploads_get(body: CreditBankStatementsUploadsGetRequest | CreditBankStatementsUploadsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditBankStatementsUploadsGetResponse`
- **Returns (raw)**: `ApiResult[CreditBankStatementsUploadsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditBankStatementsUploadsGetRequest` | `the_plaid_api/models/credit_bank_statements_uploads_get_request.py` |
| `CreditBankStatementsUploadsGetRequestDict` | `the_plaid_api/models/credit_bank_statements_uploads_get_request.py` |
| `CreditBankStatementsUploadsGetResponse` | `the_plaid_api/models/credit_bank_statements_uploads_get_response.py` |

### client.credit_employment_get

- **Route**: `POST /credit/employment/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_employment_get(body: CreditEmploymentGetRequest | CreditEmploymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditEmploymentGetResponse`
- **Returns (raw)**: `ApiResult[CreditEmploymentGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditEmploymentGetRequest` | `the_plaid_api/models/credit_employment_get_request.py` |
| `CreditEmploymentGetRequestDict` | `the_plaid_api/models/credit_employment_get_request.py` |
| `CreditEmploymentGetResponse` | `the_plaid_api/models/credit_employment_get_response.py` |

### client.credit_freddie_mac_reports_get

- **Route**: `POST /credit/freddie_mac/reports/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_freddie_mac_reports_get(body: CreditFreddieMacReportsGetRequest | CreditFreddieMacReportsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditFreddieMacReportsGetResponse`
- **Returns (raw)**: `ApiResult[CreditFreddieMacReportsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditFreddieMacReportsGetRequest` | `the_plaid_api/models/credit_freddie_mac_reports_get_request.py` |
| `CreditFreddieMacReportsGetRequestDict` | `the_plaid_api/models/credit_freddie_mac_reports_get_request.py` |
| `CreditFreddieMacReportsGetResponse` | `the_plaid_api/models/credit_freddie_mac_reports_get_response.py` |

### client.credit_payroll_income_get

- **Route**: `POST /credit/payroll_income/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_payroll_income_get(body: CreditPayrollIncomeGetRequest | CreditPayrollIncomeGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditPayrollIncomeGetResponse`
- **Returns (raw)**: `ApiResult[CreditPayrollIncomeGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditPayrollIncomeGetRequest` | `the_plaid_api/models/credit_payroll_income_get_request.py` |
| `CreditPayrollIncomeGetRequestDict` | `the_plaid_api/models/credit_payroll_income_get_request.py` |
| `CreditPayrollIncomeGetResponse` | `the_plaid_api/models/credit_payroll_income_get_response.py` |

### client.credit_payroll_income_parsing_config_update

- **Route**: `POST /credit/payroll_income/parsing_config/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_payroll_income_parsing_config_update(body: CreditPayrollIncomeParsingConfigUpdateRequest | CreditPayrollIncomeParsingConfigUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditPayrollIncomeParsingConfigUpdateResponse`
- **Returns (raw)**: `ApiResult[CreditPayrollIncomeParsingConfigUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditPayrollIncomeParsingConfigUpdateRequest` | `the_plaid_api/models/credit_payroll_income_parsing_config_update_request.py` |
| `CreditPayrollIncomeParsingConfigUpdateRequestDict` | `the_plaid_api/models/credit_payroll_income_parsing_config_update_request.py` |
| `CreditPayrollIncomeParsingConfigUpdateResponse` | `the_plaid_api/models/credit_payroll_income_parsing_config_update_response.py` |

### client.credit_payroll_income_precheck

- **Route**: `POST /credit/payroll_income/precheck`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_payroll_income_precheck(body: CreditPayrollIncomePrecheckRequest | CreditPayrollIncomePrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditPayrollIncomePrecheckResponse`
- **Returns (raw)**: `ApiResult[CreditPayrollIncomePrecheckResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditPayrollIncomePrecheckRequest` | `the_plaid_api/models/credit_payroll_income_precheck_request.py` |
| `CreditPayrollIncomePrecheckRequestDict` | `the_plaid_api/models/credit_payroll_income_precheck_request.py` |
| `CreditPayrollIncomePrecheckResponse` | `the_plaid_api/models/credit_payroll_income_precheck_response.py` |

### client.credit_payroll_income_refresh

- **Route**: `POST /credit/payroll_income/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_payroll_income_refresh(body: CreditPayrollIncomeRefreshRequest | CreditPayrollIncomeRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditPayrollIncomeRefreshResponse`
- **Returns (raw)**: `ApiResult[CreditPayrollIncomeRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditPayrollIncomeRefreshRequest` | `the_plaid_api/models/credit_payroll_income_refresh_request.py` |
| `CreditPayrollIncomeRefreshRequestDict` | `the_plaid_api/models/credit_payroll_income_refresh_request.py` |
| `CreditPayrollIncomeRefreshResponse` | `the_plaid_api/models/credit_payroll_income_refresh_response.py` |

### client.credit_payroll_income_risk_signals_get

- **Route**: `POST /credit/payroll_income/risk_signals/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_payroll_income_risk_signals_get(body: CreditPayrollIncomeRiskSignalsGetRequest | CreditPayrollIncomeRiskSignalsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditPayrollIncomeRiskSignalsGetResponse`
- **Returns (raw)**: `ApiResult[CreditPayrollIncomeRiskSignalsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditPayrollIncomeRiskSignalsGetRequest` | `the_plaid_api/models/credit_payroll_income_risk_signals_get_request.py` |
| `CreditPayrollIncomeRiskSignalsGetRequestDict` | `the_plaid_api/models/credit_payroll_income_risk_signals_get_request.py` |
| `CreditPayrollIncomeRiskSignalsGetResponse` | `the_plaid_api/models/credit_payroll_income_risk_signals_get_response.py` |

### client.credit_relay_create

- **Route**: `POST /credit/relay/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_relay_create(body: CreditRelayCreateRequest | CreditRelayCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditRelayCreateResponse`
- **Returns (raw)**: `ApiResult[CreditRelayCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditRelayCreateRequest` | `the_plaid_api/models/credit_relay_create_request.py` |
| `CreditRelayCreateRequestDict` | `the_plaid_api/models/credit_relay_create_request.py` |
| `CreditRelayCreateResponse` | `the_plaid_api/models/credit_relay_create_response.py` |

### client.credit_relay_get

- **Route**: `POST /credit/relay/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_relay_get(body: CreditRelayGetRequest | CreditRelayGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportGetResponse`
- **Returns (raw)**: `ApiResult[AssetReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditRelayGetRequest` | `the_plaid_api/models/credit_relay_get_request.py` |
| `CreditRelayGetRequestDict` | `the_plaid_api/models/credit_relay_get_request.py` |
| `AssetReportGetResponse` | `the_plaid_api/models/asset_report_get_response.py` |

### client.credit_relay_pdf_get

- **Route**: `POST /credit/relay/pdf/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_relay_pdf_get(body: CreditRelayPdfgetRequest | CreditRelayPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditRelayPdfgetRequest` | `the_plaid_api/models/credit_relay_pdfget_request.py` |
| `CreditRelayPdfgetRequestDict` | `the_plaid_api/models/credit_relay_pdfget_request.py` |

### client.credit_relay_refresh

- **Route**: `POST /credit/relay/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_relay_refresh(body: CreditRelayRefreshRequest | CreditRelayRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditRelayRefreshResponse`
- **Returns (raw)**: `ApiResult[CreditRelayRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditRelayRefreshRequest` | `the_plaid_api/models/credit_relay_refresh_request.py` |
| `CreditRelayRefreshRequestDict` | `the_plaid_api/models/credit_relay_refresh_request.py` |
| `CreditRelayRefreshResponse` | `the_plaid_api/models/credit_relay_refresh_response.py` |

### client.credit_relay_remove

- **Route**: `POST /credit/relay/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_relay_remove(body: CreditRelayRemoveRequest | CreditRelayRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditRelayRemoveResponse`
- **Returns (raw)**: `ApiResult[CreditRelayRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditRelayRemoveRequest` | `the_plaid_api/models/credit_relay_remove_request.py` |
| `CreditRelayRemoveRequestDict` | `the_plaid_api/models/credit_relay_remove_request.py` |
| `CreditRelayRemoveResponse` | `the_plaid_api/models/credit_relay_remove_response.py` |

### client.credit_report_audit_copy_remove

- **Route**: `POST /credit/audit_copy_token/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_report_audit_copy_remove(body: CreditAuditCopyTokenRemoveRequest | CreditAuditCopyTokenRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditAuditCopyTokenRemoveResponse`
- **Returns (raw)**: `ApiResult[CreditAuditCopyTokenRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditAuditCopyTokenRemoveRequest` | `the_plaid_api/models/credit_audit_copy_token_remove_request.py` |
| `CreditAuditCopyTokenRemoveRequestDict` | `the_plaid_api/models/credit_audit_copy_token_remove_request.py` |
| `CreditAuditCopyTokenRemoveResponse` | `the_plaid_api/models/credit_audit_copy_token_remove_response.py` |

### client.credit_sessions_get

- **Route**: `POST /credit/sessions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def credit_sessions_get(body: CreditSessionsGetRequest | CreditSessionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreditSessionsGetResponse`
- **Returns (raw)**: `ApiResult[CreditSessionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreditSessionsGetRequest` | `the_plaid_api/models/credit_sessions_get_request.py` |
| `CreditSessionsGetRequestDict` | `the_plaid_api/models/credit_sessions_get_request.py` |
| `CreditSessionsGetResponse` | `the_plaid_api/models/credit_sessions_get_response.py` |

### client.dashboard_user_get

- **Route**: `POST /dashboard_user/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def dashboard_user_get(body: DashboardUserGetRequest | DashboardUserGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DashboardUserGetResponse`
- **Returns (raw)**: `ApiResult[DashboardUserGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DashboardUserGetRequest` | `the_plaid_api/models/dashboard_user_get_request.py` |
| `DashboardUserGetRequestDict` | `the_plaid_api/models/dashboard_user_get_request.py` |
| `DashboardUserGetResponse` | `the_plaid_api/models/dashboard_user_get_response.py` |

### client.dashboard_user_list

- **Route**: `POST /dashboard_user/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def dashboard_user_list(body: DashboardUserListRequest | DashboardUserListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DashboardUserListResponse`
- **Returns (raw)**: `ApiResult[DashboardUserListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DashboardUserListRequest` | `the_plaid_api/models/dashboard_user_list_request.py` |
| `DashboardUserListRequestDict` | `the_plaid_api/models/dashboard_user_list_request.py` |
| `DashboardUserListResponse` | `the_plaid_api/models/dashboard_user_list_response.py` |

### client.employers_search

- **Route**: `POST /employers/search`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def employers_search(body: EmployersSearchRequest | EmployersSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `EmployersSearchResponse`
- **Returns (raw)**: `ApiResult[EmployersSearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EmployersSearchRequest` | `the_plaid_api/models/employers_search_request.py` |
| `EmployersSearchRequestDict` | `the_plaid_api/models/employers_search_request.py` |
| `EmployersSearchResponse` | `the_plaid_api/models/employers_search_response.py` |

### client.employment_verification_get

- **Route**: `POST /employment/verification/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def employment_verification_get(body: EmploymentVerificationGetRequest | EmploymentVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `EmploymentVerificationGetResponse`
- **Returns (raw)**: `ApiResult[EmploymentVerificationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EmploymentVerificationGetRequest` | `the_plaid_api/models/employment_verification_get_request.py` |
| `EmploymentVerificationGetRequestDict` | `the_plaid_api/models/employment_verification_get_request.py` |
| `EmploymentVerificationGetResponse` | `the_plaid_api/models/employment_verification_get_response.py` |

### client.fdx_consents_get

- **Route**: `GET /fdx/consents/{consentId}`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def fdx_consents_get(consent_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `consent_id`
- **Params**: `consent_id` — path `consentId`
- **Returns (parsed)**: `FdxconsentGrant`
- **Returns (raw)**: `ApiResult[FdxconsentGrant, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdxconsentGrant` | `the_plaid_api/models/fdxconsent_grant.py` |

### client.fdx_consents_list

- **Route**: `GET /fdx/consents`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def fdx_consents_list(customer_id: str, *, status: FdxConsentGrantStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`
- **Params**: `customer_id` — query `customerId` · `status` — query
- **Returns (parsed)**: `GetConsentsResponse`
- **Returns (raw)**: `ApiResult[GetConsentsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdxConsentGrantStatusOrStr` | `the_plaid_api/models/enums/fdx_consent_grant_status.py` |
| `GetConsentsResponse` | `the_plaid_api/models/get_consents_response.py` |

### client.fdx_consents_revocation_get

- **Route**: `GET /fdx/consents/{consentId}/revocation`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def fdx_consents_revocation_get(consent_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `consent_id`
- **Params**: `consent_id` — path `consentId`
- **Returns (parsed)**: `FdxconsentRevocations`
- **Returns (raw)**: `ApiResult[FdxconsentRevocations, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdxconsentRevocations` | `the_plaid_api/models/fdxconsent_revocations.py` |

### client.fdx_consents_revoke

- **Route**: `PUT /fdx/consents/{consentId}/revocation`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def fdx_consents_revoke(consent_id: str, body: FdxconsentRevocation | FdxconsentRevocationDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `consent_id`, `body`
- **Params**: `consent_id` — path `consentId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdxconsentRevocation` | `the_plaid_api/models/fdxconsent_revocation.py` |
| `FdxconsentRevocationDict` | `the_plaid_api/models/fdxconsent_revocation.py` |

### client.fdx_notifications

- **Route**: `POST /fdx/notifications`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def fdx_notifications(body: FdxNotificationEntity | FdxNotificationEntityDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdxNotificationEntity` | `the_plaid_api/models/fdx_notification_entity.py` |
| `FdxNotificationEntityDict` | `the_plaid_api/models/fdx_notification_entity.py` |

### client.get_recipient

- **Route**: `GET /fdx/recipient/{recipientId}`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def get_recipient(recipient_id: str, *, oauth_state_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `recipient_id`
- **Params**: `recipient_id` — path `recipientId` · `oauth_state_id` — header `OAUTH-STATE-ID`
- **Returns (parsed)**: `FdxrecipientMetadata`
- **Returns (raw)**: `ApiResult[FdxrecipientMetadata, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdxrecipientMetadata` | `the_plaid_api/models/fdxrecipient_metadata.py` |

### client.get_recipients

- **Route**: `GET /fdx/recipients`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def get_recipients(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GetRecipientsResponse`
- **Returns (raw)**: `ApiResult[GetRecipientsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetRecipientsResponse` | `the_plaid_api/models/get_recipients_response.py` |

### client.identity_documents_uploads_get

- **Route**: `POST /identity/documents/uploads/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_documents_uploads_get(body: IdentityDocumentsUploadsGetRequest | IdentityDocumentsUploadsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityDocumentsUploadsGetResponse`
- **Returns (raw)**: `ApiResult[IdentityDocumentsUploadsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityDocumentsUploadsGetRequest` | `the_plaid_api/models/identity_documents_uploads_get_request.py` |
| `IdentityDocumentsUploadsGetRequestDict` | `the_plaid_api/models/identity_documents_uploads_get_request.py` |
| `IdentityDocumentsUploadsGetResponse` | `the_plaid_api/models/identity_documents_uploads_get_response.py` |

### client.identity_get

- **Route**: `POST /identity/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_get(body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityGetResponse`
- **Returns (raw)**: `ApiResult[IdentityGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityGetRequest` | `the_plaid_api/models/identity_get_request.py` |
| `IdentityGetRequestDict` | `the_plaid_api/models/identity_get_request.py` |
| `IdentityGetResponse` | `the_plaid_api/models/identity_get_response.py` |

### client.identity_match

- **Route**: `POST /identity/match`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_match(body: IdentityMatchRequest | IdentityMatchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityMatchResponse`
- **Returns (raw)**: `ApiResult[IdentityMatchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityMatchRequest` | `the_plaid_api/models/identity_match_request.py` |
| `IdentityMatchRequestDict` | `the_plaid_api/models/identity_match_request.py` |
| `IdentityMatchResponse` | `the_plaid_api/models/identity_match_response.py` |

### client.identity_refresh

- **Route**: `POST /identity/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_refresh(body: IdentityRefreshRequest | IdentityRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityRefreshResponse`
- **Returns (raw)**: `ApiResult[IdentityRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityRefreshRequest` | `the_plaid_api/models/identity_refresh_request.py` |
| `IdentityRefreshRequestDict` | `the_plaid_api/models/identity_refresh_request.py` |
| `IdentityRefreshResponse` | `the_plaid_api/models/identity_refresh_response.py` |

### client.identity_verification_autofill_create

- **Route**: `POST /identity_verification/autofill/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_verification_autofill_create(body: IdentityVerificationAutofillCreateRequest | IdentityVerificationAutofillCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityVerificationAutofillCreateResponse`
- **Returns (raw)**: `ApiResult[IdentityVerificationAutofillCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityVerificationAutofillCreateRequest` | `the_plaid_api/models/identity_verification_autofill_create_request.py` |
| `IdentityVerificationAutofillCreateRequestDict` | `the_plaid_api/models/identity_verification_autofill_create_request.py` |
| `IdentityVerificationAutofillCreateResponse` | `the_plaid_api/models/identity_verification_autofill_create_response.py` |

### client.identity_verification_create

- **Route**: `POST /identity_verification/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_verification_create(body: IdentityVerificationCreateRequest | IdentityVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityVerificationCreateResponse`
- **Returns (raw)**: `ApiResult[IdentityVerificationCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityVerificationCreateRequest` | `the_plaid_api/models/identity_verification_create_request.py` |
| `IdentityVerificationCreateRequestDict` | `the_plaid_api/models/identity_verification_create_request.py` |
| `IdentityVerificationCreateResponse` | `the_plaid_api/models/identity_verification_create_response.py` |

### client.identity_verification_get

- **Route**: `POST /identity_verification/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_verification_get(body: IdentityVerificationGetRequest | IdentityVerificationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityVerificationGetResponse`
- **Returns (raw)**: `ApiResult[IdentityVerificationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityVerificationGetRequest` | `the_plaid_api/models/identity_verification_get_request.py` |
| `IdentityVerificationGetRequestDict` | `the_plaid_api/models/identity_verification_get_request.py` |
| `IdentityVerificationGetResponse` | `the_plaid_api/models/identity_verification_get_response.py` |

### client.identity_verification_list

- **Route**: `POST /identity_verification/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_verification_list(body: IdentityVerificationListRequest | IdentityVerificationListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityVerificationListResponse`
- **Returns (raw)**: `ApiResult[IdentityVerificationListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityVerificationListRequest` | `the_plaid_api/models/identity_verification_list_request.py` |
| `IdentityVerificationListRequestDict` | `the_plaid_api/models/identity_verification_list_request.py` |
| `IdentityVerificationListResponse` | `the_plaid_api/models/identity_verification_list_response.py` |

### client.identity_verification_retry

- **Route**: `POST /identity_verification/retry`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def identity_verification_retry(body: IdentityVerificationRetryRequest | IdentityVerificationRetryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityVerificationRetryResponse`
- **Returns (raw)**: `ApiResult[IdentityVerificationRetryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityVerificationRetryRequest` | `the_plaid_api/models/identity_verification_retry_request.py` |
| `IdentityVerificationRetryRequestDict` | `the_plaid_api/models/identity_verification_retry_request.py` |
| `IdentityVerificationRetryResponse` | `the_plaid_api/models/identity_verification_retry_response.py` |

### client.income_verification_create

- **Route**: `POST /income/verification/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def income_verification_create(body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationCreateResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationCreateRequest` | `the_plaid_api/models/income_verification_create_request.py` |
| `IncomeVerificationCreateRequestDict` | `the_plaid_api/models/income_verification_create_request.py` |
| `IncomeVerificationCreateResponse` | `the_plaid_api/models/income_verification_create_response.py` |

### client.income_verification_documents_download

- **Route**: `POST /income/verification/documents/download`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def income_verification_documents_download(body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationDocumentsDownloadRequest` | `the_plaid_api/models/income_verification_documents_download_request.py` |
| `IncomeVerificationDocumentsDownloadRequestDict` | `the_plaid_api/models/income_verification_documents_download_request.py` |

### client.income_verification_paystubs_get

- **Route**: `POST /income/verification/paystubs/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def income_verification_paystubs_get(body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationPaystubsGetResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationPaystubsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationPaystubsGetRequest` | `the_plaid_api/models/income_verification_paystubs_get_request.py` |
| `IncomeVerificationPaystubsGetRequestDict` | `the_plaid_api/models/income_verification_paystubs_get_request.py` |
| `IncomeVerificationPaystubsGetResponse` | `the_plaid_api/models/income_verification_paystubs_get_response.py` |

### client.income_verification_precheck

- **Route**: `POST /income/verification/precheck`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def income_verification_precheck(body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationPrecheckResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationPrecheckResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationPrecheckRequest` | `the_plaid_api/models/income_verification_precheck_request.py` |
| `IncomeVerificationPrecheckRequestDict` | `the_plaid_api/models/income_verification_precheck_request.py` |
| `IncomeVerificationPrecheckResponse` | `the_plaid_api/models/income_verification_precheck_response.py` |

### client.income_verification_taxforms_get

- **Route**: `POST /income/verification/taxforms/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def income_verification_taxforms_get(body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationTaxformsGetResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationTaxformsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationTaxformsGetRequest` | `the_plaid_api/models/income_verification_taxforms_get_request.py` |
| `IncomeVerificationTaxformsGetRequestDict` | `the_plaid_api/models/income_verification_taxforms_get_request.py` |
| `IncomeVerificationTaxformsGetResponse` | `the_plaid_api/models/income_verification_taxforms_get_response.py` |

### client.institutions_get

- **Route**: `POST /institutions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def institutions_get(body: InstitutionsGetRequest | InstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InstitutionsGetResponse`
- **Returns (raw)**: `ApiResult[InstitutionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionsGetRequest` | `the_plaid_api/models/institutions_get_request.py` |
| `InstitutionsGetRequestDict` | `the_plaid_api/models/institutions_get_request.py` |
| `InstitutionsGetResponse` | `the_plaid_api/models/institutions_get_response.py` |

### client.institutions_get_by_id

- **Route**: `POST /institutions/get_by_id`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def institutions_get_by_id(body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InstitutionsGetByIdResponse`
- **Returns (raw)**: `ApiResult[InstitutionsGetByIdResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionsGetByIdRequest` | `the_plaid_api/models/institutions_get_by_id_request.py` |
| `InstitutionsGetByIdRequestDict` | `the_plaid_api/models/institutions_get_by_id_request.py` |
| `InstitutionsGetByIdResponse` | `the_plaid_api/models/institutions_get_by_id_response.py` |

### client.institutions_search

- **Route**: `POST /institutions/search`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def institutions_search(body: InstitutionsSearchRequest | InstitutionsSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InstitutionsSearchResponse`
- **Returns (raw)**: `ApiResult[InstitutionsSearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionsSearchRequest` | `the_plaid_api/models/institutions_search_request.py` |
| `InstitutionsSearchRequestDict` | `the_plaid_api/models/institutions_search_request.py` |
| `InstitutionsSearchResponse` | `the_plaid_api/models/institutions_search_response.py` |

### client.investments_auth_get

- **Route**: `POST /investments/auth/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def investments_auth_get(body: InvestmentsAuthGetRequest | InvestmentsAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InvestmentsAuthGetResponse`
- **Returns (raw)**: `ApiResult[InvestmentsAuthGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentsAuthGetRequest` | `the_plaid_api/models/investments_auth_get_request.py` |
| `InvestmentsAuthGetRequestDict` | `the_plaid_api/models/investments_auth_get_request.py` |
| `InvestmentsAuthGetResponse` | `the_plaid_api/models/investments_auth_get_response.py` |

### client.investments_holdings_get

- **Route**: `POST /investments/holdings/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def investments_holdings_get(body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InvestmentsHoldingsGetResponse`
- **Returns (raw)**: `ApiResult[InvestmentsHoldingsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentsHoldingsGetRequest` | `the_plaid_api/models/investments_holdings_get_request.py` |
| `InvestmentsHoldingsGetRequestDict` | `the_plaid_api/models/investments_holdings_get_request.py` |
| `InvestmentsHoldingsGetResponse` | `the_plaid_api/models/investments_holdings_get_response.py` |

### client.investments_refresh

- **Route**: `POST /investments/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def investments_refresh(body: InvestmentsRefreshRequest | InvestmentsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InvestmentsRefreshResponse`
- **Returns (raw)**: `ApiResult[InvestmentsRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentsRefreshRequest` | `the_plaid_api/models/investments_refresh_request.py` |
| `InvestmentsRefreshRequestDict` | `the_plaid_api/models/investments_refresh_request.py` |
| `InvestmentsRefreshResponse` | `the_plaid_api/models/investments_refresh_response.py` |

### client.investments_transactions_get

- **Route**: `POST /investments/transactions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def investments_transactions_get(body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InvestmentsTransactionsGetResponse`
- **Returns (raw)**: `ApiResult[InvestmentsTransactionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentsTransactionsGetRequest` | `the_plaid_api/models/investments_transactions_get_request.py` |
| `InvestmentsTransactionsGetRequestDict` | `the_plaid_api/models/investments_transactions_get_request.py` |
| `InvestmentsTransactionsGetResponse` | `the_plaid_api/models/investments_transactions_get_response.py` |

### client.issues_get

- **Route**: `POST /issues/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def issues_get(body: IssuesGetRequest | IssuesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IssuesGetResponse`
- **Returns (raw)**: `ApiResult[IssuesGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IssuesGetRequest` | `the_plaid_api/models/issues_get_request.py` |
| `IssuesGetRequestDict` | `the_plaid_api/models/issues_get_request.py` |
| `IssuesGetResponse` | `the_plaid_api/models/issues_get_response.py` |

### client.issues_search

- **Route**: `POST /issues/search`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def issues_search(body: IssuesSearchRequest | IssuesSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IssuesSearchResponse`
- **Returns (raw)**: `ApiResult[IssuesSearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IssuesSearchRequest` | `the_plaid_api/models/issues_search_request.py` |
| `IssuesSearchRequestDict` | `the_plaid_api/models/issues_search_request.py` |
| `IssuesSearchResponse` | `the_plaid_api/models/issues_search_response.py` |

### client.issues_subscribe

- **Route**: `POST /issues/subscribe`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def issues_subscribe(body: IssuesSubscribeRequest | IssuesSubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IssuesSubscribeResponse`
- **Returns (raw)**: `ApiResult[IssuesSubscribeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IssuesSubscribeRequest` | `the_plaid_api/models/issues_subscribe_request.py` |
| `IssuesSubscribeRequestDict` | `the_plaid_api/models/issues_subscribe_request.py` |
| `IssuesSubscribeResponse` | `the_plaid_api/models/issues_subscribe_response.py` |

### client.item_access_token_invalidate

- **Route**: `POST /item/access_token/invalidate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_access_token_invalidate(body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemAccessTokenInvalidateResponse`
- **Returns (raw)**: `ApiResult[ItemAccessTokenInvalidateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemAccessTokenInvalidateRequest` | `the_plaid_api/models/item_access_token_invalidate_request.py` |
| `ItemAccessTokenInvalidateRequestDict` | `the_plaid_api/models/item_access_token_invalidate_request.py` |
| `ItemAccessTokenInvalidateResponse` | `the_plaid_api/models/item_access_token_invalidate_response.py` |

### client.item_activity_list

- **Route**: `POST /item/activity/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_activity_list(body: ItemActivityListRequest | ItemActivityListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemActivityListResponse`
- **Returns (raw)**: `ApiResult[ItemActivityListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemActivityListRequest` | `the_plaid_api/models/item_activity_list_request.py` |
| `ItemActivityListRequestDict` | `the_plaid_api/models/item_activity_list_request.py` |
| `ItemActivityListResponse` | `the_plaid_api/models/item_activity_list_response.py` |

### client.item_application_list

- **Route**: `POST /item/application/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_application_list(body: ItemApplicationListRequest | ItemApplicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemApplicationListResponse`
- **Returns (raw)**: `ApiResult[ItemApplicationListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemApplicationListRequest` | `the_plaid_api/models/item_application_list_request.py` |
| `ItemApplicationListRequestDict` | `the_plaid_api/models/item_application_list_request.py` |
| `ItemApplicationListResponse` | `the_plaid_api/models/item_application_list_response.py` |

### client.item_application_scopes_update

- **Route**: `POST /item/application/scopes/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_application_scopes_update(body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemApplicationScopesUpdateResponse`
- **Returns (raw)**: `ApiResult[ItemApplicationScopesUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemApplicationScopesUpdateRequest` | `the_plaid_api/models/item_application_scopes_update_request.py` |
| `ItemApplicationScopesUpdateRequestDict` | `the_plaid_api/models/item_application_scopes_update_request.py` |
| `ItemApplicationScopesUpdateResponse` | `the_plaid_api/models/item_application_scopes_update_response.py` |

### client.item_application_unlink

- **Route**: `POST /item/application/unlink`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_application_unlink(body: ItemApplicationUnlinkRequest | ItemApplicationUnlinkRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemApplicationUnlinkResponse`
- **Returns (raw)**: `ApiResult[ItemApplicationUnlinkResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemApplicationUnlinkRequest` | `the_plaid_api/models/item_application_unlink_request.py` |
| `ItemApplicationUnlinkRequestDict` | `the_plaid_api/models/item_application_unlink_request.py` |
| `ItemApplicationUnlinkResponse` | `the_plaid_api/models/item_application_unlink_response.py` |

### client.item_create_public_token

- **Route**: `POST /item/public_token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_create_public_token(body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemPublicTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ItemPublicTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemPublicTokenCreateRequest` | `the_plaid_api/models/item_public_token_create_request.py` |
| `ItemPublicTokenCreateRequestDict` | `the_plaid_api/models/item_public_token_create_request.py` |
| `ItemPublicTokenCreateResponse` | `the_plaid_api/models/item_public_token_create_response.py` |

### client.item_get

- **Route**: `POST /item/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_get(body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemGetResponse`
- **Returns (raw)**: `ApiResult[ItemGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemGetRequest` | `the_plaid_api/models/item_get_request.py` |
| `ItemGetRequestDict` | `the_plaid_api/models/item_get_request.py` |
| `ItemGetResponse` | `the_plaid_api/models/item_get_response.py` |

### client.item_import

- **Route**: `POST /item/import`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_import(body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemImportResponse`
- **Returns (raw)**: `ApiResult[ItemImportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemImportRequest` | `the_plaid_api/models/item_import_request.py` |
| `ItemImportRequestDict` | `the_plaid_api/models/item_import_request.py` |
| `ItemImportResponse` | `the_plaid_api/models/item_import_response.py` |

### client.item_products_terminate

- **Route**: `POST /item/products/terminate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_products_terminate(body: ItemProductsTerminateRequest | ItemProductsTerminateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemProductsTerminateResponse`
- **Returns (raw)**: `ApiResult[ItemProductsTerminateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemProductsTerminateRequest` | `the_plaid_api/models/item_products_terminate_request.py` |
| `ItemProductsTerminateRequestDict` | `the_plaid_api/models/item_products_terminate_request.py` |
| `ItemProductsTerminateResponse` | `the_plaid_api/models/item_products_terminate_response.py` |

### client.item_public_token_exchange

- **Route**: `POST /item/public_token/exchange`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_public_token_exchange(body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemPublicTokenExchangeResponse`
- **Returns (raw)**: `ApiResult[ItemPublicTokenExchangeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemPublicTokenExchangeRequest` | `the_plaid_api/models/item_public_token_exchange_request.py` |
| `ItemPublicTokenExchangeRequestDict` | `the_plaid_api/models/item_public_token_exchange_request.py` |
| `ItemPublicTokenExchangeResponse` | `the_plaid_api/models/item_public_token_exchange_response.py` |

### client.item_remove

- **Route**: `POST /item/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_remove(body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemRemoveResponse`
- **Returns (raw)**: `ApiResult[ItemRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemRemoveRequest` | `the_plaid_api/models/item_remove_request.py` |
| `ItemRemoveRequestDict` | `the_plaid_api/models/item_remove_request.py` |
| `ItemRemoveResponse` | `the_plaid_api/models/item_remove_response.py` |

### client.item_webhook_update

- **Route**: `POST /item/webhook/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def item_webhook_update(body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemWebhookUpdateResponse`
- **Returns (raw)**: `ApiResult[ItemWebhookUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemWebhookUpdateRequest` | `the_plaid_api/models/item_webhook_update_request.py` |
| `ItemWebhookUpdateRequestDict` | `the_plaid_api/models/item_webhook_update_request.py` |
| `ItemWebhookUpdateResponse` | `the_plaid_api/models/item_webhook_update_response.py` |

### client.liabilities_get

- **Route**: `POST /liabilities/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def liabilities_get(body: LiabilitiesGetRequest | LiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LiabilitiesGetResponse`
- **Returns (raw)**: `ApiResult[LiabilitiesGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LiabilitiesGetRequest` | `the_plaid_api/models/liabilities_get_request.py` |
| `LiabilitiesGetRequestDict` | `the_plaid_api/models/liabilities_get_request.py` |
| `LiabilitiesGetResponse` | `the_plaid_api/models/liabilities_get_response.py` |

### client.link_delivery_create

- **Route**: `POST /link_delivery/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def link_delivery_create(body: LinkDeliveryCreateRequest | LinkDeliveryCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LinkDeliveryCreateResponse`
- **Returns (raw)**: `ApiResult[LinkDeliveryCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkDeliveryCreateRequest` | `the_plaid_api/models/link_delivery_create_request.py` |
| `LinkDeliveryCreateRequestDict` | `the_plaid_api/models/link_delivery_create_request.py` |
| `LinkDeliveryCreateResponse` | `the_plaid_api/models/link_delivery_create_response.py` |

### client.link_delivery_get

- **Route**: `POST /link_delivery/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def link_delivery_get(body: LinkDeliveryGetRequest | LinkDeliveryGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LinkDeliveryGetResponse`
- **Returns (raw)**: `ApiResult[LinkDeliveryGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkDeliveryGetRequest` | `the_plaid_api/models/link_delivery_get_request.py` |
| `LinkDeliveryGetRequestDict` | `the_plaid_api/models/link_delivery_get_request.py` |
| `LinkDeliveryGetResponse` | `the_plaid_api/models/link_delivery_get_response.py` |

### client.link_oauth_correlation_id_exchange

- **Route**: `POST /link/oauth/correlation_id/exchange`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def link_oauth_correlation_id_exchange(body: LinkOauthCorrelationIdExchangeRequest | LinkOauthCorrelationIdExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LinkOauthCorrelationIdExchangeResponse`
- **Returns (raw)**: `ApiResult[LinkOauthCorrelationIdExchangeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkOauthCorrelationIdExchangeRequest` | `the_plaid_api/models/link_oauth_correlation_id_exchange_request.py` |
| `LinkOauthCorrelationIdExchangeRequestDict` | `the_plaid_api/models/link_oauth_correlation_id_exchange_request.py` |
| `LinkOauthCorrelationIdExchangeResponse` | `the_plaid_api/models/link_oauth_correlation_id_exchange_response.py` |

### client.link_token_create

- **Route**: `POST /link/token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def link_token_create(body: LinkTokenCreateRequest | LinkTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LinkTokenCreateResponse`
- **Returns (raw)**: `ApiResult[LinkTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkTokenCreateRequest` | `the_plaid_api/models/link_token_create_request.py` |
| `LinkTokenCreateRequestDict` | `the_plaid_api/models/link_token_create_request.py` |
| `LinkTokenCreateResponse` | `the_plaid_api/models/link_token_create_response.py` |

### client.link_token_get

- **Route**: `POST /link/token/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def link_token_get(body: LinkTokenGetRequest | LinkTokenGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LinkTokenGetResponse`
- **Returns (raw)**: `ApiResult[LinkTokenGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkTokenGetRequest` | `the_plaid_api/models/link_token_get_request.py` |
| `LinkTokenGetRequestDict` | `the_plaid_api/models/link_token_get_request.py` |
| `LinkTokenGetResponse` | `the_plaid_api/models/link_token_get_response.py` |

### client.network_status_get

- **Route**: `POST /network/status/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def network_status_get(body: NetworkStatusGetRequest | NetworkStatusGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NetworkStatusGetResponse`
- **Returns (raw)**: `ApiResult[NetworkStatusGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NetworkStatusGetRequest` | `the_plaid_api/models/network_status_get_request.py` |
| `NetworkStatusGetRequestDict` | `the_plaid_api/models/network_status_get_request.py` |
| `NetworkStatusGetResponse` | `the_plaid_api/models/network_status_get_response.py` |

### client.oauth_introspect

- **Route**: `POST /oauth/introspect`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def oauth_introspect(body: OauthIntrospectRequest | OauthIntrospectRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `OauthIntrospectResponse`
- **Returns (raw)**: `ApiResult[OauthIntrospectResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OauthIntrospectRequest` | `the_plaid_api/models/oauth_introspect_request.py` |
| `OauthIntrospectRequestDict` | `the_plaid_api/models/oauth_introspect_request.py` |
| `OauthIntrospectResponse` | `the_plaid_api/models/oauth_introspect_response.py` |

### client.oauth_revoke

- **Route**: `POST /oauth/revoke`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def oauth_revoke(body: OauthRevokeRequest | OauthRevokeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `OauthRevokeResponse`
- **Returns (raw)**: `ApiResult[OauthRevokeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OauthRevokeRequest` | `the_plaid_api/models/oauth_revoke_request.py` |
| `OauthRevokeRequestDict` | `the_plaid_api/models/oauth_revoke_request.py` |
| `OauthRevokeResponse` | `the_plaid_api/models/oauth_revoke_response.py` |

### client.oauth_token

- **Route**: `POST /oauth/token`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def oauth_token(body: OauthTokenRequest | OauthTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `OauthTokenResponse`
- **Returns (raw)**: `ApiResult[OauthTokenResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OauthTokenRequest` | `the_plaid_api/models/oauth_token_request.py` |
| `OauthTokenRequestDict` | `the_plaid_api/models/oauth_token_request.py` |
| `OauthTokenResponse` | `the_plaid_api/models/oauth_token_response.py` |

### client.partner_customer_create

- **Route**: `POST /partner/customer/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def partner_customer_create(body: PartnerCustomerCreateRequest | PartnerCustomerCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PartnerCustomerCreateResponse`
- **Returns (raw)**: `ApiResult[PartnerCustomerCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PartnerCustomerCreateRequest` | `the_plaid_api/models/partner_customer_create_request.py` |
| `PartnerCustomerCreateRequestDict` | `the_plaid_api/models/partner_customer_create_request.py` |
| `PartnerCustomerCreateResponse` | `the_plaid_api/models/partner_customer_create_response.py` |

### client.partner_customer_enable

- **Route**: `POST /partner/customer/enable`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def partner_customer_enable(body: PartnerCustomerEnableRequest | PartnerCustomerEnableRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PartnerCustomerEnableResponse`
- **Returns (raw)**: `ApiResult[PartnerCustomerEnableResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PartnerCustomerEnableRequest` | `the_plaid_api/models/partner_customer_enable_request.py` |
| `PartnerCustomerEnableRequestDict` | `the_plaid_api/models/partner_customer_enable_request.py` |
| `PartnerCustomerEnableResponse` | `the_plaid_api/models/partner_customer_enable_response.py` |

### client.partner_customer_get

- **Route**: `POST /partner/customer/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def partner_customer_get(body: PartnerCustomerGetRequest | PartnerCustomerGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PartnerCustomerGetResponse`
- **Returns (raw)**: `ApiResult[PartnerCustomerGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PartnerCustomerGetRequest` | `the_plaid_api/models/partner_customer_get_request.py` |
| `PartnerCustomerGetRequestDict` | `the_plaid_api/models/partner_customer_get_request.py` |
| `PartnerCustomerGetResponse` | `the_plaid_api/models/partner_customer_get_response.py` |

### client.partner_customer_oauth_institutions_get

- **Route**: `POST /partner/customer/oauth_institutions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def partner_customer_oauth_institutions_get(body: PartnerCustomerOauthInstitutionsGetRequest | PartnerCustomerOauthInstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PartnerCustomerOauthInstitutionsGetResponse`
- **Returns (raw)**: `ApiResult[PartnerCustomerOauthInstitutionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PartnerCustomerOauthInstitutionsGetRequest` | `the_plaid_api/models/partner_customer_oauth_institutions_get_request.py` |
| `PartnerCustomerOauthInstitutionsGetRequestDict` | `the_plaid_api/models/partner_customer_oauth_institutions_get_request.py` |
| `PartnerCustomerOauthInstitutionsGetResponse` | `the_plaid_api/models/partner_customer_oauth_institutions_get_response.py` |

### client.partner_customer_remove

- **Route**: `POST /partner/customer/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def partner_customer_remove(body: PartnerCustomerRemoveRequest | PartnerCustomerRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PartnerCustomerRemoveResponse`
- **Returns (raw)**: `ApiResult[PartnerCustomerRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PartnerCustomerRemoveRequest` | `the_plaid_api/models/partner_customer_remove_request.py` |
| `PartnerCustomerRemoveRequestDict` | `the_plaid_api/models/partner_customer_remove_request.py` |
| `PartnerCustomerRemoveResponse` | `the_plaid_api/models/partner_customer_remove_response.py` |

### client.payment_initiation_consent_create

- **Route**: `POST /payment_initiation/consent/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_consent_create(body: PaymentInitiationConsentCreateRequest | PaymentInitiationConsentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationConsentCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationConsentCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationConsentCreateRequest` | `the_plaid_api/models/payment_initiation_consent_create_request.py` |
| `PaymentInitiationConsentCreateRequestDict` | `the_plaid_api/models/payment_initiation_consent_create_request.py` |
| `PaymentInitiationConsentCreateResponse` | `the_plaid_api/models/payment_initiation_consent_create_response.py` |

### client.payment_initiation_consent_get

- **Route**: `POST /payment_initiation/consent/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_consent_get(body: PaymentInitiationConsentGetRequest | PaymentInitiationConsentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationConsentGetResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationConsentGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationConsentGetRequest` | `the_plaid_api/models/payment_initiation_consent_get_request.py` |
| `PaymentInitiationConsentGetRequestDict` | `the_plaid_api/models/payment_initiation_consent_get_request.py` |
| `PaymentInitiationConsentGetResponse` | `the_plaid_api/models/payment_initiation_consent_get_response.py` |

### client.payment_initiation_consent_payment_execute

- **Route**: `POST /payment_initiation/consent/payment/execute`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_consent_payment_execute(body: PaymentInitiationConsentPaymentExecuteRequest | PaymentInitiationConsentPaymentExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationConsentPaymentExecuteResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationConsentPaymentExecuteResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationConsentPaymentExecuteRequest` | `the_plaid_api/models/payment_initiation_consent_payment_execute_request.py` |
| `PaymentInitiationConsentPaymentExecuteRequestDict` | `the_plaid_api/models/payment_initiation_consent_payment_execute_request.py` |
| `PaymentInitiationConsentPaymentExecuteResponse` | `the_plaid_api/models/payment_initiation_consent_payment_execute_response.py` |

### client.payment_initiation_consent_revoke

- **Route**: `POST /payment_initiation/consent/revoke`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_consent_revoke(body: PaymentInitiationConsentRevokeRequest | PaymentInitiationConsentRevokeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationConsentRevokeResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationConsentRevokeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationConsentRevokeRequest` | `the_plaid_api/models/payment_initiation_consent_revoke_request.py` |
| `PaymentInitiationConsentRevokeRequestDict` | `the_plaid_api/models/payment_initiation_consent_revoke_request.py` |
| `PaymentInitiationConsentRevokeResponse` | `the_plaid_api/models/payment_initiation_consent_revoke_response.py` |

### client.payment_initiation_payment_create

- **Route**: `POST /payment_initiation/payment/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_payment_create(body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentCreateRequest` | `the_plaid_api/models/payment_initiation_payment_create_request.py` |
| `PaymentInitiationPaymentCreateRequestDict` | `the_plaid_api/models/payment_initiation_payment_create_request.py` |
| `PaymentInitiationPaymentCreateResponse` | `the_plaid_api/models/payment_initiation_payment_create_response.py` |

### client.payment_initiation_payment_get

- **Route**: `POST /payment_initiation/payment/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_payment_get(body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentGetResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentGetRequest` | `the_plaid_api/models/payment_initiation_payment_get_request.py` |
| `PaymentInitiationPaymentGetRequestDict` | `the_plaid_api/models/payment_initiation_payment_get_request.py` |
| `PaymentInitiationPaymentGetResponse` | `the_plaid_api/models/payment_initiation_payment_get_response.py` |

### client.payment_initiation_payment_list

- **Route**: `POST /payment_initiation/payment/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_payment_list(body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentListResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentListRequest` | `the_plaid_api/models/payment_initiation_payment_list_request.py` |
| `PaymentInitiationPaymentListRequestDict` | `the_plaid_api/models/payment_initiation_payment_list_request.py` |
| `PaymentInitiationPaymentListResponse` | `the_plaid_api/models/payment_initiation_payment_list_response.py` |

### client.payment_initiation_payment_reverse

- **Route**: `POST /payment_initiation/payment/reverse`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_payment_reverse(body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentReverseResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentReverseResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentReverseRequest` | `the_plaid_api/models/payment_initiation_payment_reverse_request.py` |
| `PaymentInitiationPaymentReverseRequestDict` | `the_plaid_api/models/payment_initiation_payment_reverse_request.py` |
| `PaymentInitiationPaymentReverseResponse` | `the_plaid_api/models/payment_initiation_payment_reverse_response.py` |

### client.payment_initiation_recipient_create

- **Route**: `POST /payment_initiation/recipient/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_recipient_create(body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationRecipientCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationRecipientCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationRecipientCreateRequest` | `the_plaid_api/models/payment_initiation_recipient_create_request.py` |
| `PaymentInitiationRecipientCreateRequestDict` | `the_plaid_api/models/payment_initiation_recipient_create_request.py` |
| `PaymentInitiationRecipientCreateResponse` | `the_plaid_api/models/payment_initiation_recipient_create_response.py` |

### client.payment_initiation_recipient_get

- **Route**: `POST /payment_initiation/recipient/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_recipient_get(body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationRecipientGetResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationRecipientGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationRecipientGetRequest` | `the_plaid_api/models/payment_initiation_recipient_get_request.py` |
| `PaymentInitiationRecipientGetRequestDict` | `the_plaid_api/models/payment_initiation_recipient_get_request.py` |
| `PaymentInitiationRecipientGetResponse` | `the_plaid_api/models/payment_initiation_recipient_get_response.py` |

### client.payment_initiation_recipient_list

- **Route**: `POST /payment_initiation/recipient/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_initiation_recipient_list(body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationRecipientListResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationRecipientListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationRecipientListRequest` | `the_plaid_api/models/payment_initiation_recipient_list_request.py` |
| `PaymentInitiationRecipientListRequestDict` | `the_plaid_api/models/payment_initiation_recipient_list_request.py` |
| `PaymentInitiationRecipientListResponse` | `the_plaid_api/models/payment_initiation_recipient_list_response.py` |

### client.payment_profile_create

- **Route**: `POST /payment_profile/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_profile_create(body: PaymentProfileCreateRequest | PaymentProfileCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentProfileCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentProfileCreateRequest` | `the_plaid_api/models/payment_profile_create_request.py` |
| `PaymentProfileCreateRequestDict` | `the_plaid_api/models/payment_profile_create_request.py` |
| `PaymentProfileCreateResponse` | `the_plaid_api/models/payment_profile_create_response.py` |

### client.payment_profile_get

- **Route**: `POST /payment_profile/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_profile_get(body: PaymentProfileGetRequest | PaymentProfileGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentProfileGetResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentProfileGetRequest` | `the_plaid_api/models/payment_profile_get_request.py` |
| `PaymentProfileGetRequestDict` | `the_plaid_api/models/payment_profile_get_request.py` |
| `PaymentProfileGetResponse` | `the_plaid_api/models/payment_profile_get_response.py` |

### client.payment_profile_remove

- **Route**: `POST /payment_profile/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def payment_profile_remove(body: PaymentProfileRemoveRequest | PaymentProfileRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentProfileRemoveResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentProfileRemoveRequest` | `the_plaid_api/models/payment_profile_remove_request.py` |
| `PaymentProfileRemoveRequestDict` | `the_plaid_api/models/payment_profile_remove_request.py` |
| `PaymentProfileRemoveResponse` | `the_plaid_api/models/payment_profile_remove_response.py` |

### client.processor_account_get

- **Route**: `POST /processor/account/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_account_get(body: ProcessorAccountGetRequest | ProcessorAccountGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorAccountGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorAccountGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorAccountGetRequest` | `the_plaid_api/models/processor_account_get_request.py` |
| `ProcessorAccountGetRequestDict` | `the_plaid_api/models/processor_account_get_request.py` |
| `ProcessorAccountGetResponse` | `the_plaid_api/models/processor_account_get_response.py` |

### client.processor_apex_processor_token_create

- **Route**: `POST /processor/apex/processor_token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_apex_processor_token_create(body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorApexProcessorTokenCreateRequest` | `the_plaid_api/models/processor_apex_processor_token_create_request.py` |
| `ProcessorApexProcessorTokenCreateRequestDict` | `the_plaid_api/models/processor_apex_processor_token_create_request.py` |
| `ProcessorTokenCreateResponse` | `the_plaid_api/models/processor_token_create_response.py` |

### client.processor_auth_get

- **Route**: `POST /processor/auth/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_auth_get(body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorAuthGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorAuthGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorAuthGetRequest` | `the_plaid_api/models/processor_auth_get_request.py` |
| `ProcessorAuthGetRequestDict` | `the_plaid_api/models/processor_auth_get_request.py` |
| `ProcessorAuthGetResponse` | `the_plaid_api/models/processor_auth_get_response.py` |

### client.processor_balance_get

- **Route**: `POST /processor/balance/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_balance_get(body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorBalanceGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorBalanceGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorBalanceGetRequest` | `the_plaid_api/models/processor_balance_get_request.py` |
| `ProcessorBalanceGetRequestDict` | `the_plaid_api/models/processor_balance_get_request.py` |
| `ProcessorBalanceGetResponse` | `the_plaid_api/models/processor_balance_get_response.py` |

### client.processor_bank_transfer_create

- **Route**: `POST /processor/bank_transfer/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_bank_transfer_create(body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorBankTransferCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorBankTransferCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorBankTransferCreateRequest` | `the_plaid_api/models/processor_bank_transfer_create_request.py` |
| `ProcessorBankTransferCreateRequestDict` | `the_plaid_api/models/processor_bank_transfer_create_request.py` |
| `ProcessorBankTransferCreateResponse` | `the_plaid_api/models/processor_bank_transfer_create_response.py` |

### client.processor_identity_get

- **Route**: `POST /processor/identity/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_identity_get(body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorIdentityGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorIdentityGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorIdentityGetRequest` | `the_plaid_api/models/processor_identity_get_request.py` |
| `ProcessorIdentityGetRequestDict` | `the_plaid_api/models/processor_identity_get_request.py` |
| `ProcessorIdentityGetResponse` | `the_plaid_api/models/processor_identity_get_response.py` |

### client.processor_identity_match

- **Route**: `POST /processor/identity/match`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_identity_match(body: ProcessorIdentityMatchRequest | ProcessorIdentityMatchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorIdentityMatchResponse`
- **Returns (raw)**: `ApiResult[ProcessorIdentityMatchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorIdentityMatchRequest` | `the_plaid_api/models/processor_identity_match_request.py` |
| `ProcessorIdentityMatchRequestDict` | `the_plaid_api/models/processor_identity_match_request.py` |
| `ProcessorIdentityMatchResponse` | `the_plaid_api/models/processor_identity_match_response.py` |

### client.processor_investments_auth_get

- **Route**: `POST /processor/investments/auth/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_investments_auth_get(body: ProcessorInvestmentsAuthGetRequest | ProcessorInvestmentsAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorInvestmentsAuthGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorInvestmentsAuthGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorInvestmentsAuthGetRequest` | `the_plaid_api/models/processor_investments_auth_get_request.py` |
| `ProcessorInvestmentsAuthGetRequestDict` | `the_plaid_api/models/processor_investments_auth_get_request.py` |
| `ProcessorInvestmentsAuthGetResponse` | `the_plaid_api/models/processor_investments_auth_get_response.py` |

### client.processor_investments_holdings_get

- **Route**: `POST /processor/investments/holdings/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_investments_holdings_get(body: ProcessorInvestmentsHoldingsGetRequest | ProcessorInvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorInvestmentsHoldingsGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorInvestmentsHoldingsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorInvestmentsHoldingsGetRequest` | `the_plaid_api/models/processor_investments_holdings_get_request.py` |
| `ProcessorInvestmentsHoldingsGetRequestDict` | `the_plaid_api/models/processor_investments_holdings_get_request.py` |
| `ProcessorInvestmentsHoldingsGetResponse` | `the_plaid_api/models/processor_investments_holdings_get_response.py` |

### client.processor_investments_transactions_get

- **Route**: `POST /processor/investments/transactions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_investments_transactions_get(body: ProcessorInvestmentsTransactionsGetRequest | ProcessorInvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorInvestmentsTransactionsGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorInvestmentsTransactionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorInvestmentsTransactionsGetRequest` | `the_plaid_api/models/processor_investments_transactions_get_request.py` |
| `ProcessorInvestmentsTransactionsGetRequestDict` | `the_plaid_api/models/processor_investments_transactions_get_request.py` |
| `ProcessorInvestmentsTransactionsGetResponse` | `the_plaid_api/models/processor_investments_transactions_get_response.py` |

### client.processor_liabilities_get

- **Route**: `POST /processor/liabilities/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_liabilities_get(body: ProcessorLiabilitiesGetRequest | ProcessorLiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorLiabilitiesGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorLiabilitiesGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorLiabilitiesGetRequest` | `the_plaid_api/models/processor_liabilities_get_request.py` |
| `ProcessorLiabilitiesGetRequestDict` | `the_plaid_api/models/processor_liabilities_get_request.py` |
| `ProcessorLiabilitiesGetResponse` | `the_plaid_api/models/processor_liabilities_get_response.py` |

### client.processor_signal_decision_report

- **Route**: `POST /processor/signal/decision/report`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_signal_decision_report(body: ProcessorSignalDecisionReportRequest | ProcessorSignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorSignalDecisionReportResponse`
- **Returns (raw)**: `ApiResult[ProcessorSignalDecisionReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorSignalDecisionReportRequest` | `the_plaid_api/models/processor_signal_decision_report_request.py` |
| `ProcessorSignalDecisionReportRequestDict` | `the_plaid_api/models/processor_signal_decision_report_request.py` |
| `ProcessorSignalDecisionReportResponse` | `the_plaid_api/models/processor_signal_decision_report_response.py` |

### client.processor_signal_evaluate

- **Route**: `POST /processor/signal/evaluate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_signal_evaluate(body: ProcessorSignalEvaluateRequest | ProcessorSignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorSignalEvaluateResponse`
- **Returns (raw)**: `ApiResult[ProcessorSignalEvaluateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorSignalEvaluateRequest` | `the_plaid_api/models/processor_signal_evaluate_request.py` |
| `ProcessorSignalEvaluateRequestDict` | `the_plaid_api/models/processor_signal_evaluate_request.py` |
| `ProcessorSignalEvaluateResponse` | `the_plaid_api/models/processor_signal_evaluate_response.py` |

### client.processor_signal_prepare

- **Route**: `POST /processor/signal/prepare`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_signal_prepare(body: ProcessorSignalPrepareRequest | ProcessorSignalPrepareRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorSignalPrepareResponse`
- **Returns (raw)**: `ApiResult[ProcessorSignalPrepareResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorSignalPrepareRequest` | `the_plaid_api/models/processor_signal_prepare_request.py` |
| `ProcessorSignalPrepareRequestDict` | `the_plaid_api/models/processor_signal_prepare_request.py` |
| `ProcessorSignalPrepareResponse` | `the_plaid_api/models/processor_signal_prepare_response.py` |

### client.processor_signal_return_report

- **Route**: `POST /processor/signal/return/report`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_signal_return_report(body: ProcessorSignalReturnReportRequest | ProcessorSignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorSignalReturnReportResponse`
- **Returns (raw)**: `ApiResult[ProcessorSignalReturnReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorSignalReturnReportRequest` | `the_plaid_api/models/processor_signal_return_report_request.py` |
| `ProcessorSignalReturnReportRequestDict` | `the_plaid_api/models/processor_signal_return_report_request.py` |
| `ProcessorSignalReturnReportResponse` | `the_plaid_api/models/processor_signal_return_report_response.py` |

### client.processor_stripe_bank_account_token_create

- **Route**: `POST /processor/stripe/bank_account_token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_stripe_bank_account_token_create(body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorStripeBankAccountTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorStripeBankAccountTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorStripeBankAccountTokenCreateRequest` | `the_plaid_api/models/processor_stripe_bank_account_token_create_request.py` |
| `ProcessorStripeBankAccountTokenCreateRequestDict` | `the_plaid_api/models/processor_stripe_bank_account_token_create_request.py` |
| `ProcessorStripeBankAccountTokenCreateResponse` | `the_plaid_api/models/processor_stripe_bank_account_token_create_response.py` |

### client.processor_token_create

- **Route**: `POST /processor/token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_token_create(body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTokenCreateRequest` | `the_plaid_api/models/processor_token_create_request.py` |
| `ProcessorTokenCreateRequestDict` | `the_plaid_api/models/processor_token_create_request.py` |
| `ProcessorTokenCreateResponse` | `the_plaid_api/models/processor_token_create_response.py` |

### client.processor_token_permissions_get

- **Route**: `POST /processor/token/permissions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_token_permissions_get(body: ProcessorTokenPermissionsGetRequest | ProcessorTokenPermissionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTokenPermissionsGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorTokenPermissionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTokenPermissionsGetRequest` | `the_plaid_api/models/processor_token_permissions_get_request.py` |
| `ProcessorTokenPermissionsGetRequestDict` | `the_plaid_api/models/processor_token_permissions_get_request.py` |
| `ProcessorTokenPermissionsGetResponse` | `the_plaid_api/models/processor_token_permissions_get_response.py` |

### client.processor_token_permissions_set

- **Route**: `POST /processor/token/permissions/set`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_token_permissions_set(body: ProcessorTokenPermissionsSetRequest | ProcessorTokenPermissionsSetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTokenPermissionsSetResponse`
- **Returns (raw)**: `ApiResult[ProcessorTokenPermissionsSetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTokenPermissionsSetRequest` | `the_plaid_api/models/processor_token_permissions_set_request.py` |
| `ProcessorTokenPermissionsSetRequestDict` | `the_plaid_api/models/processor_token_permissions_set_request.py` |
| `ProcessorTokenPermissionsSetResponse` | `the_plaid_api/models/processor_token_permissions_set_response.py` |

### client.processor_token_webhook_update

- **Route**: `POST /processor/token/webhook/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_token_webhook_update(body: ProcessorTokenWebhookUpdateRequest | ProcessorTokenWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTokenWebhookUpdateResponse`
- **Returns (raw)**: `ApiResult[ProcessorTokenWebhookUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTokenWebhookUpdateRequest` | `the_plaid_api/models/processor_token_webhook_update_request.py` |
| `ProcessorTokenWebhookUpdateRequestDict` | `the_plaid_api/models/processor_token_webhook_update_request.py` |
| `ProcessorTokenWebhookUpdateResponse` | `the_plaid_api/models/processor_token_webhook_update_response.py` |

### client.processor_transactions_get

- **Route**: `POST /processor/transactions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_transactions_get(body: ProcessorTransactionsGetRequest | ProcessorTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTransactionsGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorTransactionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTransactionsGetRequest` | `the_plaid_api/models/processor_transactions_get_request.py` |
| `ProcessorTransactionsGetRequestDict` | `the_plaid_api/models/processor_transactions_get_request.py` |
| `ProcessorTransactionsGetResponse` | `the_plaid_api/models/processor_transactions_get_response.py` |

### client.processor_transactions_recurring_get

- **Route**: `POST /processor/transactions/recurring/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_transactions_recurring_get(body: ProcessorTransactionsRecurringGetRequest | ProcessorTransactionsRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTransactionsRecurringGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorTransactionsRecurringGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTransactionsRecurringGetRequest` | `the_plaid_api/models/processor_transactions_recurring_get_request.py` |
| `ProcessorTransactionsRecurringGetRequestDict` | `the_plaid_api/models/processor_transactions_recurring_get_request.py` |
| `ProcessorTransactionsRecurringGetResponse` | `the_plaid_api/models/processor_transactions_recurring_get_response.py` |

### client.processor_transactions_refresh

- **Route**: `POST /processor/transactions/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_transactions_refresh(body: ProcessorTransactionsRefreshRequest | ProcessorTransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTransactionsRefreshResponse`
- **Returns (raw)**: `ApiResult[ProcessorTransactionsRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTransactionsRefreshRequest` | `the_plaid_api/models/processor_transactions_refresh_request.py` |
| `ProcessorTransactionsRefreshRequestDict` | `the_plaid_api/models/processor_transactions_refresh_request.py` |
| `ProcessorTransactionsRefreshResponse` | `the_plaid_api/models/processor_transactions_refresh_response.py` |

### client.processor_transactions_sync

- **Route**: `POST /processor/transactions/sync`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def processor_transactions_sync(body: ProcessorTransactionsSyncRequest | ProcessorTransactionsSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTransactionsSyncResponse`
- **Returns (raw)**: `ApiResult[ProcessorTransactionsSyncResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTransactionsSyncRequest` | `the_plaid_api/models/processor_transactions_sync_request.py` |
| `ProcessorTransactionsSyncRequestDict` | `the_plaid_api/models/processor_transactions_sync_request.py` |
| `ProcessorTransactionsSyncResponse` | `the_plaid_api/models/processor_transactions_sync_response.py` |

### client.profile_network_status_get

- **Route**: `POST /profile/network_status/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def profile_network_status_get(body: ProfileNetworkStatusGetRequest | ProfileNetworkStatusGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProfileNetworkStatusGetResponse`
- **Returns (raw)**: `ApiResult[ProfileNetworkStatusGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProfileNetworkStatusGetRequest` | `the_plaid_api/models/profile_network_status_get_request.py` |
| `ProfileNetworkStatusGetRequestDict` | `the_plaid_api/models/profile_network_status_get_request.py` |
| `ProfileNetworkStatusGetResponse` | `the_plaid_api/models/profile_network_status_get_response.py` |

### client.protect_compute

- **Route**: `POST /protect/compute`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def protect_compute(body: ProtectComputeRequest | ProtectComputeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProtectComputeResponse`
- **Returns (raw)**: `ApiResult[ProtectComputeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProtectComputeRequest` | `the_plaid_api/models/protect_compute_request.py` |
| `ProtectComputeRequestDict` | `the_plaid_api/models/protect_compute_request.py` |
| `ProtectComputeResponse` | `the_plaid_api/models/protect_compute_response.py` |

### client.protect_event_get

- **Route**: `POST /protect/event/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def protect_event_get(body: ProtectEventGetRequest | ProtectEventGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProtectEventGetResponse`
- **Returns (raw)**: `ApiResult[ProtectEventGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProtectEventGetRequest` | `the_plaid_api/models/protect_event_get_request.py` |
| `ProtectEventGetRequestDict` | `the_plaid_api/models/protect_event_get_request.py` |
| `ProtectEventGetResponse` | `the_plaid_api/models/protect_event_get_response.py` |

### client.protect_event_send

- **Route**: `POST /protect/event/send`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def protect_event_send(body: ProtectEventSendRequest | ProtectEventSendRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProtectEventSendResponse`
- **Returns (raw)**: `ApiResult[ProtectEventSendResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProtectEventSendRequest` | `the_plaid_api/models/protect_event_send_request.py` |
| `ProtectEventSendRequestDict` | `the_plaid_api/models/protect_event_send_request.py` |
| `ProtectEventSendResponse` | `the_plaid_api/models/protect_event_send_response.py` |

### client.protect_report_create

- **Route**: `POST /protect/report/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def protect_report_create(body: ProtectReportCreateRequest | ProtectReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProtectReportCreateResponse`
- **Returns (raw)**: `ApiResult[ProtectReportCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProtectReportCreateRequest` | `the_plaid_api/models/protect_report_create_request.py` |
| `ProtectReportCreateRequestDict` | `the_plaid_api/models/protect_report_create_request.py` |
| `ProtectReportCreateResponse` | `the_plaid_api/models/protect_report_create_response.py` |

### client.protect_user_insights_get

- **Route**: `POST /protect/user/insights/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def protect_user_insights_get(body: ProtectUserInsightsGetRequest | ProtectUserInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProtectUserInsightsGetResponse`
- **Returns (raw)**: `ApiResult[ProtectUserInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProtectUserInsightsGetRequest` | `the_plaid_api/models/protect_user_insights_get_request.py` |
| `ProtectUserInsightsGetRequestDict` | `the_plaid_api/models/protect_user_insights_get_request.py` |
| `ProtectUserInsightsGetResponse` | `the_plaid_api/models/protect_user_insights_get_response.py` |

### client.sandbox_bank_income_fire_webhook

- **Route**: `POST /sandbox/bank_income/fire_webhook`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_bank_income_fire_webhook(body: SandboxBankIncomeFireWebhookRequest | SandboxBankIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxBankIncomeFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxBankIncomeFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxBankIncomeFireWebhookRequest` | `the_plaid_api/models/sandbox_bank_income_fire_webhook_request.py` |
| `SandboxBankIncomeFireWebhookRequestDict` | `the_plaid_api/models/sandbox_bank_income_fire_webhook_request.py` |
| `SandboxBankIncomeFireWebhookResponse` | `the_plaid_api/models/sandbox_bank_income_fire_webhook_response.py` |

### client.sandbox_bank_transfer_fire_webhook

- **Route**: `POST /sandbox/bank_transfer/fire_webhook`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_bank_transfer_fire_webhook(body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxBankTransferFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxBankTransferFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxBankTransferFireWebhookRequest` | `the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py` |
| `SandboxBankTransferFireWebhookRequestDict` | `the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py` |
| `SandboxBankTransferFireWebhookResponse` | `the_plaid_api/models/sandbox_bank_transfer_fire_webhook_response.py` |

### client.sandbox_bank_transfer_simulate

- **Route**: `POST /sandbox/bank_transfer/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_bank_transfer_simulate(body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxBankTransferSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxBankTransferSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxBankTransferSimulateRequest` | `the_plaid_api/models/sandbox_bank_transfer_simulate_request.py` |
| `SandboxBankTransferSimulateRequestDict` | `the_plaid_api/models/sandbox_bank_transfer_simulate_request.py` |
| `SandboxBankTransferSimulateResponse` | `the_plaid_api/models/sandbox_bank_transfer_simulate_response.py` |

### client.sandbox_cra_cashflow_updates_update

- **Route**: `POST /sandbox/cra/cashflow_updates/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_cra_cashflow_updates_update(body: SandboxCraCashflowUpdatesUpdateRequest | SandboxCraCashflowUpdatesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxCraCashflowUpdatesUpdateResponse`
- **Returns (raw)**: `ApiResult[SandboxCraCashflowUpdatesUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxCraCashflowUpdatesUpdateRequest` | `the_plaid_api/models/sandbox_cra_cashflow_updates_update_request.py` |
| `SandboxCraCashflowUpdatesUpdateRequestDict` | `the_plaid_api/models/sandbox_cra_cashflow_updates_update_request.py` |
| `SandboxCraCashflowUpdatesUpdateResponse` | `the_plaid_api/models/sandbox_cra_cashflow_updates_update_response.py` |

### client.sandbox_fdx_consent_seed

- **Route**: `POST /sandbox/fdx/consent/seed`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_fdx_consent_seed(body: SandboxFdxConsentSeedRequest | SandboxFdxConsentSeedRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxFdxConsentSeedResponse`
- **Returns (raw)**: `ApiResult[SandboxFdxConsentSeedResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxFdxConsentSeedRequest` | `the_plaid_api/models/sandbox_fdx_consent_seed_request.py` |
| `SandboxFdxConsentSeedRequestDict` | `the_plaid_api/models/sandbox_fdx_consent_seed_request.py` |
| `SandboxFdxConsentSeedResponse` | `the_plaid_api/models/sandbox_fdx_consent_seed_response.py` |

### client.sandbox_income_fire_webhook

- **Route**: `POST /sandbox/income/fire_webhook`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_income_fire_webhook(body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxIncomeFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxIncomeFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxIncomeFireWebhookRequest` | `the_plaid_api/models/sandbox_income_fire_webhook_request.py` |
| `SandboxIncomeFireWebhookRequestDict` | `the_plaid_api/models/sandbox_income_fire_webhook_request.py` |
| `SandboxIncomeFireWebhookResponse` | `the_plaid_api/models/sandbox_income_fire_webhook_response.py` |

### client.sandbox_item_application_seed

- **Route**: `POST /sandbox/item/application/seed`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_item_application_seed(body: SandboxItemApplicationSeedRequest | SandboxItemApplicationSeedRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxItemApplicationSeedResponse`
- **Returns (raw)**: `ApiResult[SandboxItemApplicationSeedResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxItemApplicationSeedRequest` | `the_plaid_api/models/sandbox_item_application_seed_request.py` |
| `SandboxItemApplicationSeedRequestDict` | `the_plaid_api/models/sandbox_item_application_seed_request.py` |
| `SandboxItemApplicationSeedResponse` | `the_plaid_api/models/sandbox_item_application_seed_response.py` |

### client.sandbox_item_fire_webhook

- **Route**: `POST /sandbox/item/fire_webhook`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_item_fire_webhook(body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxItemFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxItemFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxItemFireWebhookRequest` | `the_plaid_api/models/sandbox_item_fire_webhook_request.py` |
| `SandboxItemFireWebhookRequestDict` | `the_plaid_api/models/sandbox_item_fire_webhook_request.py` |
| `SandboxItemFireWebhookResponse` | `the_plaid_api/models/sandbox_item_fire_webhook_response.py` |

### client.sandbox_item_reset_login

- **Route**: `POST /sandbox/item/reset_login`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_item_reset_login(body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxItemResetLoginResponse`
- **Returns (raw)**: `ApiResult[SandboxItemResetLoginResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxItemResetLoginRequest` | `the_plaid_api/models/sandbox_item_reset_login_request.py` |
| `SandboxItemResetLoginRequestDict` | `the_plaid_api/models/sandbox_item_reset_login_request.py` |
| `SandboxItemResetLoginResponse` | `the_plaid_api/models/sandbox_item_reset_login_response.py` |

### client.sandbox_item_set_verification_status

- **Route**: `POST /sandbox/item/set_verification_status`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_item_set_verification_status(body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxItemSetVerificationStatusResponse`
- **Returns (raw)**: `ApiResult[SandboxItemSetVerificationStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxItemSetVerificationStatusRequest` | `the_plaid_api/models/sandbox_item_set_verification_status_request.py` |
| `SandboxItemSetVerificationStatusRequestDict` | `the_plaid_api/models/sandbox_item_set_verification_status_request.py` |
| `SandboxItemSetVerificationStatusResponse` | `the_plaid_api/models/sandbox_item_set_verification_status_response.py` |

### client.sandbox_oauth_select_accounts

- **Route**: `POST /sandbox/oauth/select_accounts`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_oauth_select_accounts(body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxOauthSelectAccountsRequest` | `the_plaid_api/models/sandbox_oauth_select_accounts_request.py` |
| `SandboxOauthSelectAccountsRequestDict` | `the_plaid_api/models/sandbox_oauth_select_accounts_request.py` |

### client.sandbox_payment_profile_reset_login

- **Route**: `POST /sandbox/payment_profile/reset_login`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_payment_profile_reset_login(body: SandboxPaymentProfileResetLoginRequest | SandboxPaymentProfileResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxPaymentProfileResetLoginResponse`
- **Returns (raw)**: `ApiResult[SandboxPaymentProfileResetLoginResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxPaymentProfileResetLoginRequest` | `the_plaid_api/models/sandbox_payment_profile_reset_login_request.py` |
| `SandboxPaymentProfileResetLoginRequestDict` | `the_plaid_api/models/sandbox_payment_profile_reset_login_request.py` |
| `SandboxPaymentProfileResetLoginResponse` | `the_plaid_api/models/sandbox_payment_profile_reset_login_response.py` |

### client.sandbox_payment_simulate

- **Route**: `POST /sandbox/payment/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_payment_simulate(body: SandboxPaymentSimulateRequest | SandboxPaymentSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxPaymentSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxPaymentSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxPaymentSimulateRequest` | `the_plaid_api/models/sandbox_payment_simulate_request.py` |
| `SandboxPaymentSimulateRequestDict` | `the_plaid_api/models/sandbox_payment_simulate_request.py` |
| `SandboxPaymentSimulateResponse` | `the_plaid_api/models/sandbox_payment_simulate_response.py` |

### client.sandbox_processor_token_create

- **Route**: `POST /sandbox/processor_token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_processor_token_create(body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxProcessorTokenCreateResponse`
- **Returns (raw)**: `ApiResult[SandboxProcessorTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxProcessorTokenCreateRequest` | `the_plaid_api/models/sandbox_processor_token_create_request.py` |
| `SandboxProcessorTokenCreateRequestDict` | `the_plaid_api/models/sandbox_processor_token_create_request.py` |
| `SandboxProcessorTokenCreateResponse` | `the_plaid_api/models/sandbox_processor_token_create_response.py` |

### client.sandbox_public_token_create

- **Route**: `POST /sandbox/public_token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_public_token_create(body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxPublicTokenCreateResponse`
- **Returns (raw)**: `ApiResult[SandboxPublicTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxPublicTokenCreateRequest` | `the_plaid_api/models/sandbox_public_token_create_request.py` |
| `SandboxPublicTokenCreateRequestDict` | `the_plaid_api/models/sandbox_public_token_create_request.py` |
| `SandboxPublicTokenCreateResponse` | `the_plaid_api/models/sandbox_public_token_create_response.py` |

### client.sandbox_transactions_create

- **Route**: `POST /sandbox/transactions/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transactions_create(body: SandboxTransactionsCreateRequest | SandboxTransactionsCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransactionsCreateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransactionsCreateResponse, SandboxTransactionsCreateErrorBody]`
- **Error**: `SandboxTransactionsCreateErrorBody` — **Case A (typed)**
- **Error arms**: `Error | None` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SandboxTransactionsCreateRequest` | `the_plaid_api/models/sandbox_transactions_create_request.py` |
| `SandboxTransactionsCreateRequestDict` | `the_plaid_api/models/sandbox_transactions_create_request.py` |
| `SandboxTransactionsCreateResponse` | `the_plaid_api/models/sandbox_transactions_create_response.py` |
| `SandboxTransactionsCreateErrorBody` | `the_plaid_api/errors/sandbox_transactions_create_error.py` |
| `Error` | `the_plaid_api/models/error.py` |

### client.sandbox_transfer_fire_webhook

- **Route**: `POST /sandbox/transfer/fire_webhook`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_fire_webhook(body: SandboxTransferFireWebhookRequest | SandboxTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferFireWebhookRequest` | `the_plaid_api/models/sandbox_transfer_fire_webhook_request.py` |
| `SandboxTransferFireWebhookRequestDict` | `the_plaid_api/models/sandbox_transfer_fire_webhook_request.py` |
| `SandboxTransferFireWebhookResponse` | `the_plaid_api/models/sandbox_transfer_fire_webhook_response.py` |

### client.sandbox_transfer_ledger_deposit_simulate

- **Route**: `POST /sandbox/transfer/ledger/deposit/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_ledger_deposit_simulate(body: SandboxTransferLedgerDepositSimulateRequest | SandboxTransferLedgerDepositSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferLedgerDepositSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferLedgerDepositSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferLedgerDepositSimulateRequest` | `the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_request.py` |
| `SandboxTransferLedgerDepositSimulateRequestDict` | `the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_request.py` |
| `SandboxTransferLedgerDepositSimulateResponse` | `the_plaid_api/models/sandbox_transfer_ledger_deposit_simulate_response.py` |

### client.sandbox_transfer_ledger_simulate_available

- **Route**: `POST /sandbox/transfer/ledger/simulate_available`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_ledger_simulate_available(body: SandboxTransferLedgerSimulateAvailableRequest | SandboxTransferLedgerSimulateAvailableRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferLedgerSimulateAvailableResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferLedgerSimulateAvailableResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferLedgerSimulateAvailableRequest` | `the_plaid_api/models/sandbox_transfer_ledger_simulate_available_request.py` |
| `SandboxTransferLedgerSimulateAvailableRequestDict` | `the_plaid_api/models/sandbox_transfer_ledger_simulate_available_request.py` |
| `SandboxTransferLedgerSimulateAvailableResponse` | `the_plaid_api/models/sandbox_transfer_ledger_simulate_available_response.py` |

### client.sandbox_transfer_ledger_withdraw_simulate

- **Route**: `POST /sandbox/transfer/ledger/withdraw/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_ledger_withdraw_simulate(body: SandboxTransferLedgerWithdrawSimulateRequest | SandboxTransferLedgerWithdrawSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferLedgerWithdrawSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferLedgerWithdrawSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferLedgerWithdrawSimulateRequest` | `the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_request.py` |
| `SandboxTransferLedgerWithdrawSimulateRequestDict` | `the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_request.py` |
| `SandboxTransferLedgerWithdrawSimulateResponse` | `the_plaid_api/models/sandbox_transfer_ledger_withdraw_simulate_response.py` |

### client.sandbox_transfer_refund_simulate

- **Route**: `POST /sandbox/transfer/refund/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_refund_simulate(body: SandboxTransferRefundSimulateRequest | SandboxTransferRefundSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferRefundSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferRefundSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferRefundSimulateRequest` | `the_plaid_api/models/sandbox_transfer_refund_simulate_request.py` |
| `SandboxTransferRefundSimulateRequestDict` | `the_plaid_api/models/sandbox_transfer_refund_simulate_request.py` |
| `SandboxTransferRefundSimulateResponse` | `the_plaid_api/models/sandbox_transfer_refund_simulate_response.py` |

### client.sandbox_transfer_repayment_simulate

- **Route**: `POST /sandbox/transfer/repayment/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_repayment_simulate(body: SandboxTransferRepaymentSimulateRequest | SandboxTransferRepaymentSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferRepaymentSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferRepaymentSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferRepaymentSimulateRequest` | `the_plaid_api/models/sandbox_transfer_repayment_simulate_request.py` |
| `SandboxTransferRepaymentSimulateRequestDict` | `the_plaid_api/models/sandbox_transfer_repayment_simulate_request.py` |
| `SandboxTransferRepaymentSimulateResponse` | `the_plaid_api/models/sandbox_transfer_repayment_simulate_response.py` |

### client.sandbox_transfer_simulate

- **Route**: `POST /sandbox/transfer/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_simulate(body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferSimulateRequest` | `the_plaid_api/models/sandbox_transfer_simulate_request.py` |
| `SandboxTransferSimulateRequestDict` | `the_plaid_api/models/sandbox_transfer_simulate_request.py` |
| `SandboxTransferSimulateResponse` | `the_plaid_api/models/sandbox_transfer_simulate_response.py` |

### client.sandbox_transfer_sweep_simulate

- **Route**: `POST /sandbox/transfer/sweep/simulate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_sweep_simulate(body: SandboxTransferSweepSimulateRequest | SandboxTransferSweepSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferSweepSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferSweepSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferSweepSimulateRequest` | `the_plaid_api/models/sandbox_transfer_sweep_simulate_request.py` |
| `SandboxTransferSweepSimulateRequestDict` | `the_plaid_api/models/sandbox_transfer_sweep_simulate_request.py` |
| `SandboxTransferSweepSimulateResponse` | `the_plaid_api/models/sandbox_transfer_sweep_simulate_response.py` |

### client.sandbox_transfer_test_clock_advance

- **Route**: `POST /sandbox/transfer/test_clock/advance`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_test_clock_advance(body: SandboxTransferTestClockAdvanceRequest | SandboxTransferTestClockAdvanceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferTestClockAdvanceResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferTestClockAdvanceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferTestClockAdvanceRequest` | `the_plaid_api/models/sandbox_transfer_test_clock_advance_request.py` |
| `SandboxTransferTestClockAdvanceRequestDict` | `the_plaid_api/models/sandbox_transfer_test_clock_advance_request.py` |
| `SandboxTransferTestClockAdvanceResponse` | `the_plaid_api/models/sandbox_transfer_test_clock_advance_response.py` |

### client.sandbox_transfer_test_clock_create

- **Route**: `POST /sandbox/transfer/test_clock/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_test_clock_create(body: SandboxTransferTestClockCreateRequest | SandboxTransferTestClockCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferTestClockCreateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferTestClockCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferTestClockCreateRequest` | `the_plaid_api/models/sandbox_transfer_test_clock_create_request.py` |
| `SandboxTransferTestClockCreateRequestDict` | `the_plaid_api/models/sandbox_transfer_test_clock_create_request.py` |
| `SandboxTransferTestClockCreateResponse` | `the_plaid_api/models/sandbox_transfer_test_clock_create_response.py` |

### client.sandbox_transfer_test_clock_get

- **Route**: `POST /sandbox/transfer/test_clock/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_test_clock_get(body: SandboxTransferTestClockGetRequest | SandboxTransferTestClockGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferTestClockGetResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferTestClockGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferTestClockGetRequest` | `the_plaid_api/models/sandbox_transfer_test_clock_get_request.py` |
| `SandboxTransferTestClockGetRequestDict` | `the_plaid_api/models/sandbox_transfer_test_clock_get_request.py` |
| `SandboxTransferTestClockGetResponse` | `the_plaid_api/models/sandbox_transfer_test_clock_get_response.py` |

### client.sandbox_transfer_test_clock_list

- **Route**: `POST /sandbox/transfer/test_clock/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_transfer_test_clock_list(body: SandboxTransferTestClockListRequest | SandboxTransferTestClockListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferTestClockListResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferTestClockListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferTestClockListRequest` | `the_plaid_api/models/sandbox_transfer_test_clock_list_request.py` |
| `SandboxTransferTestClockListRequestDict` | `the_plaid_api/models/sandbox_transfer_test_clock_list_request.py` |
| `SandboxTransferTestClockListResponse` | `the_plaid_api/models/sandbox_transfer_test_clock_list_response.py` |

### client.sandbox_user_reset_login

- **Route**: `POST /sandbox/user/reset_login`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def sandbox_user_reset_login(body: SandboxUserResetLoginRequest | SandboxUserResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxUserResetLoginResponse`
- **Returns (raw)**: `ApiResult[SandboxUserResetLoginResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxUserResetLoginRequest` | `the_plaid_api/models/sandbox_user_reset_login_request.py` |
| `SandboxUserResetLoginRequestDict` | `the_plaid_api/models/sandbox_user_reset_login_request.py` |
| `SandboxUserResetLoginResponse` | `the_plaid_api/models/sandbox_user_reset_login_response.py` |

### client.session_token_create

- **Route**: `POST /session/token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def session_token_create(body: SessionTokenCreateRequest | SessionTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SessionTokenCreateResponse`
- **Returns (raw)**: `ApiResult[SessionTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SessionTokenCreateRequest` | `the_plaid_api/models/session_token_create_request.py` |
| `SessionTokenCreateRequestDict` | `the_plaid_api/models/session_token_create_request.py` |
| `SessionTokenCreateResponse` | `the_plaid_api/models/session_token_create_response.py` |

### client.signal_decision_report

- **Route**: `POST /signal/decision/report`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def signal_decision_report(body: SignalDecisionReportRequest | SignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalDecisionReportResponse`
- **Returns (raw)**: `ApiResult[SignalDecisionReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalDecisionReportRequest` | `the_plaid_api/models/signal_decision_report_request.py` |
| `SignalDecisionReportRequestDict` | `the_plaid_api/models/signal_decision_report_request.py` |
| `SignalDecisionReportResponse` | `the_plaid_api/models/signal_decision_report_response.py` |

### client.signal_evaluate

- **Route**: `POST /signal/evaluate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def signal_evaluate(body: SignalEvaluateRequest | SignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalEvaluateResponse`
- **Returns (raw)**: `ApiResult[SignalEvaluateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalEvaluateRequest` | `the_plaid_api/models/signal_evaluate_request.py` |
| `SignalEvaluateRequestDict` | `the_plaid_api/models/signal_evaluate_request.py` |
| `SignalEvaluateResponse` | `the_plaid_api/models/signal_evaluate_response.py` |

### client.signal_prepare

- **Route**: `POST /signal/prepare`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def signal_prepare(body: SignalPrepareRequest | SignalPrepareRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalPrepareResponse`
- **Returns (raw)**: `ApiResult[SignalPrepareResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalPrepareRequest` | `the_plaid_api/models/signal_prepare_request.py` |
| `SignalPrepareRequestDict` | `the_plaid_api/models/signal_prepare_request.py` |
| `SignalPrepareResponse` | `the_plaid_api/models/signal_prepare_response.py` |

### client.signal_return_report

- **Route**: `POST /signal/return/report`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def signal_return_report(body: SignalReturnReportRequest | SignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalReturnReportResponse`
- **Returns (raw)**: `ApiResult[SignalReturnReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalReturnReportRequest` | `the_plaid_api/models/signal_return_report_request.py` |
| `SignalReturnReportRequestDict` | `the_plaid_api/models/signal_return_report_request.py` |
| `SignalReturnReportResponse` | `the_plaid_api/models/signal_return_report_response.py` |

### client.signal_schedule

- **Route**: `POST /signal/schedule`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def signal_schedule(body: SignalScheduleRequest | SignalScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalScheduleResponse`
- **Returns (raw)**: `ApiResult[SignalScheduleResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalScheduleRequest` | `the_plaid_api/models/signal_schedule_request.py` |
| `SignalScheduleRequestDict` | `the_plaid_api/models/signal_schedule_request.py` |
| `SignalScheduleResponse` | `the_plaid_api/models/signal_schedule_response.py` |

### client.statements_download

- **Route**: `POST /statements/download`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def statements_download(body: StatementsDownloadRequest | StatementsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatementsDownloadRequest` | `the_plaid_api/models/statements_download_request.py` |
| `StatementsDownloadRequestDict` | `the_plaid_api/models/statements_download_request.py` |

### client.statements_list

- **Route**: `POST /statements/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def statements_list(body: StatementsListRequest | StatementsListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StatementsListResponse`
- **Returns (raw)**: `ApiResult[StatementsListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatementsListRequest` | `the_plaid_api/models/statements_list_request.py` |
| `StatementsListRequestDict` | `the_plaid_api/models/statements_list_request.py` |
| `StatementsListResponse` | `the_plaid_api/models/statements_list_response.py` |

### client.statements_refresh

- **Route**: `POST /statements/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def statements_refresh(body: StatementsRefreshRequest | StatementsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StatementsRefreshResponse`
- **Returns (raw)**: `ApiResult[StatementsRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatementsRefreshRequest` | `the_plaid_api/models/statements_refresh_request.py` |
| `StatementsRefreshRequestDict` | `the_plaid_api/models/statements_refresh_request.py` |
| `StatementsRefreshResponse` | `the_plaid_api/models/statements_refresh_response.py` |

### client.transactions_enhance

- **Route**: `POST /beta/transactions/v1/enhance`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_enhance(body: TransactionsEnhanceGetRequest | TransactionsEnhanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsEnhanceGetResponse`
- **Returns (raw)**: `ApiResult[TransactionsEnhanceGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsEnhanceGetRequest` | `the_plaid_api/models/transactions_enhance_get_request.py` |
| `TransactionsEnhanceGetRequestDict` | `the_plaid_api/models/transactions_enhance_get_request.py` |
| `TransactionsEnhanceGetResponse` | `the_plaid_api/models/transactions_enhance_get_response.py` |

### client.transactions_enrich

- **Route**: `POST /transactions/enrich`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_enrich(body: TransactionsEnrichRequest | TransactionsEnrichRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsEnrichResponse`
- **Returns (raw)**: `ApiResult[TransactionsEnrichResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsEnrichRequest` | `the_plaid_api/models/transactions_enrich_request.py` |
| `TransactionsEnrichRequestDict` | `the_plaid_api/models/transactions_enrich_request.py` |
| `TransactionsEnrichResponse` | `the_plaid_api/models/transactions_enrich_response.py` |

### client.transactions_get

- **Route**: `POST /transactions/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_get(body: TransactionsGetRequest | TransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsGetResponse`
- **Returns (raw)**: `ApiResult[TransactionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsGetRequest` | `the_plaid_api/models/transactions_get_request.py` |
| `TransactionsGetRequestDict` | `the_plaid_api/models/transactions_get_request.py` |
| `TransactionsGetResponse` | `the_plaid_api/models/transactions_get_response.py` |

### client.transactions_recurring_get

- **Route**: `POST /transactions/recurring/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_recurring_get(body: TransactionsRecurringGetRequest | TransactionsRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsRecurringGetResponse`
- **Returns (raw)**: `ApiResult[TransactionsRecurringGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsRecurringGetRequest` | `the_plaid_api/models/transactions_recurring_get_request.py` |
| `TransactionsRecurringGetRequestDict` | `the_plaid_api/models/transactions_recurring_get_request.py` |
| `TransactionsRecurringGetResponse` | `the_plaid_api/models/transactions_recurring_get_response.py` |

### client.transactions_refresh

- **Route**: `POST /transactions/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_refresh(body: TransactionsRefreshRequest | TransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsRefreshResponse`
- **Returns (raw)**: `ApiResult[TransactionsRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsRefreshRequest` | `the_plaid_api/models/transactions_refresh_request.py` |
| `TransactionsRefreshRequestDict` | `the_plaid_api/models/transactions_refresh_request.py` |
| `TransactionsRefreshResponse` | `the_plaid_api/models/transactions_refresh_response.py` |

### client.transactions_rules_create

- **Route**: `POST /beta/transactions/rules/v1/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_rules_create(body: TransactionsRulesCreateRequest | TransactionsRulesCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsRulesCreateResponse`
- **Returns (raw)**: `ApiResult[TransactionsRulesCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsRulesCreateRequest` | `the_plaid_api/models/transactions_rules_create_request.py` |
| `TransactionsRulesCreateRequestDict` | `the_plaid_api/models/transactions_rules_create_request.py` |
| `TransactionsRulesCreateResponse` | `the_plaid_api/models/transactions_rules_create_response.py` |

### client.transactions_rules_list

- **Route**: `POST /beta/transactions/rules/v1/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_rules_list(body: TransactionsRulesListRequest | TransactionsRulesListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsRulesListResponse`
- **Returns (raw)**: `ApiResult[TransactionsRulesListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsRulesListRequest` | `the_plaid_api/models/transactions_rules_list_request.py` |
| `TransactionsRulesListRequestDict` | `the_plaid_api/models/transactions_rules_list_request.py` |
| `TransactionsRulesListResponse` | `the_plaid_api/models/transactions_rules_list_response.py` |

### client.transactions_rules_remove

- **Route**: `POST /beta/transactions/rules/v1/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_rules_remove(body: TransactionsRulesRemoveRequest | TransactionsRulesRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsRulesRemoveResponse`
- **Returns (raw)**: `ApiResult[TransactionsRulesRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsRulesRemoveRequest` | `the_plaid_api/models/transactions_rules_remove_request.py` |
| `TransactionsRulesRemoveRequestDict` | `the_plaid_api/models/transactions_rules_remove_request.py` |
| `TransactionsRulesRemoveResponse` | `the_plaid_api/models/transactions_rules_remove_response.py` |

### client.transactions_sync

- **Route**: `POST /transactions/sync`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_sync(body: TransactionsSyncRequest | TransactionsSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsSyncResponse`
- **Returns (raw)**: `ApiResult[TransactionsSyncResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsSyncRequest` | `the_plaid_api/models/transactions_sync_request.py` |
| `TransactionsSyncRequestDict` | `the_plaid_api/models/transactions_sync_request.py` |
| `TransactionsSyncResponse` | `the_plaid_api/models/transactions_sync_response.py` |

### client.transactions_user_insights_get

- **Route**: `POST /beta/transactions/user_insights/v1/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transactions_user_insights_get(body: TransactionsUserInsightsGetRequest | TransactionsUserInsightsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsUserInsightsGetResponse`
- **Returns (raw)**: `ApiResult[TransactionsUserInsightsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsUserInsightsGetRequest` | `the_plaid_api/models/transactions_user_insights_get_request.py` |
| `TransactionsUserInsightsGetRequestDict` | `the_plaid_api/models/transactions_user_insights_get_request.py` |
| `TransactionsUserInsightsGetResponse` | `the_plaid_api/models/transactions_user_insights_get_response.py` |

### client.transfer_authorization_cancel

- **Route**: `POST /transfer/authorization/cancel`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_authorization_cancel(body: TransferAuthorizationCancelRequest | TransferAuthorizationCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferAuthorizationCancelResponse`
- **Returns (raw)**: `ApiResult[TransferAuthorizationCancelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferAuthorizationCancelRequest` | `the_plaid_api/models/transfer_authorization_cancel_request.py` |
| `TransferAuthorizationCancelRequestDict` | `the_plaid_api/models/transfer_authorization_cancel_request.py` |
| `TransferAuthorizationCancelResponse` | `the_plaid_api/models/transfer_authorization_cancel_response.py` |

### client.transfer_authorization_create

- **Route**: `POST /transfer/authorization/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_authorization_create(body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferAuthorizationCreateResponse`
- **Returns (raw)**: `ApiResult[TransferAuthorizationCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferAuthorizationCreateRequest` | `the_plaid_api/models/transfer_authorization_create_request.py` |
| `TransferAuthorizationCreateRequestDict` | `the_plaid_api/models/transfer_authorization_create_request.py` |
| `TransferAuthorizationCreateResponse` | `the_plaid_api/models/transfer_authorization_create_response.py` |

### client.transfer_balance_get

- **Route**: `POST /transfer/balance/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_balance_get(body: TransferBalanceGetRequest | TransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferBalanceGetResponse`
- **Returns (raw)**: `ApiResult[TransferBalanceGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferBalanceGetRequest` | `the_plaid_api/models/transfer_balance_get_request.py` |
| `TransferBalanceGetRequestDict` | `the_plaid_api/models/transfer_balance_get_request.py` |
| `TransferBalanceGetResponse` | `the_plaid_api/models/transfer_balance_get_response.py` |

### client.transfer_cancel

- **Route**: `POST /transfer/cancel`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_cancel(body: TransferCancelRequest | TransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferCancelResponse`
- **Returns (raw)**: `ApiResult[TransferCancelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferCancelRequest` | `the_plaid_api/models/transfer_cancel_request.py` |
| `TransferCancelRequestDict` | `the_plaid_api/models/transfer_cancel_request.py` |
| `TransferCancelResponse` | `the_plaid_api/models/transfer_cancel_response.py` |

### client.transfer_capabilities_get

- **Route**: `POST /transfer/capabilities/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_capabilities_get(body: TransferCapabilitiesGetRequest | TransferCapabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferCapabilitiesGetResponse`
- **Returns (raw)**: `ApiResult[TransferCapabilitiesGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferCapabilitiesGetRequest` | `the_plaid_api/models/transfer_capabilities_get_request.py` |
| `TransferCapabilitiesGetRequestDict` | `the_plaid_api/models/transfer_capabilities_get_request.py` |
| `TransferCapabilitiesGetResponse` | `the_plaid_api/models/transfer_capabilities_get_response.py` |

### client.transfer_configuration_get

- **Route**: `POST /transfer/configuration/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_configuration_get(body: TransferConfigurationGetRequest | TransferConfigurationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferConfigurationGetResponse`
- **Returns (raw)**: `ApiResult[TransferConfigurationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferConfigurationGetRequest` | `the_plaid_api/models/transfer_configuration_get_request.py` |
| `TransferConfigurationGetRequestDict` | `the_plaid_api/models/transfer_configuration_get_request.py` |
| `TransferConfigurationGetResponse` | `the_plaid_api/models/transfer_configuration_get_response.py` |

### client.transfer_create

- **Route**: `POST /transfer/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_create(body: TransferCreateRequest | TransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferCreateResponse`
- **Returns (raw)**: `ApiResult[TransferCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferCreateRequest` | `the_plaid_api/models/transfer_create_request.py` |
| `TransferCreateRequestDict` | `the_plaid_api/models/transfer_create_request.py` |
| `TransferCreateResponse` | `the_plaid_api/models/transfer_create_response.py` |

### client.transfer_diligence_document_upload

- **Route**: `POST /transfer/diligence/document/upload`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_diligence_document_upload(body: TransferDiligenceDocumentUploadRequest | TransferDiligenceDocumentUploadRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferDiligenceDocumentUploadResponse`
- **Returns (raw)**: `ApiResult[TransferDiligenceDocumentUploadResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferDiligenceDocumentUploadRequest` | `the_plaid_api/models/transfer_diligence_document_upload_request.py` |
| `TransferDiligenceDocumentUploadRequestDict` | `the_plaid_api/models/transfer_diligence_document_upload_request.py` |
| `TransferDiligenceDocumentUploadResponse` | `the_plaid_api/models/transfer_diligence_document_upload_response.py` |

### client.transfer_diligence_submit

- **Route**: `POST /transfer/diligence/submit`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_diligence_submit(body: TransferDiligenceSubmitRequest | TransferDiligenceSubmitRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferDiligenceSubmitResponse`
- **Returns (raw)**: `ApiResult[TransferDiligenceSubmitResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferDiligenceSubmitRequest` | `the_plaid_api/models/transfer_diligence_submit_request.py` |
| `TransferDiligenceSubmitRequestDict` | `the_plaid_api/models/transfer_diligence_submit_request.py` |
| `TransferDiligenceSubmitResponse` | `the_plaid_api/models/transfer_diligence_submit_response.py` |

### client.transfer_event_list

- **Route**: `POST /transfer/event/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_event_list(body: TransferEventListRequest | TransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferEventListResponse`
- **Returns (raw)**: `ApiResult[TransferEventListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferEventListRequest` | `the_plaid_api/models/transfer_event_list_request.py` |
| `TransferEventListRequestDict` | `the_plaid_api/models/transfer_event_list_request.py` |
| `TransferEventListResponse` | `the_plaid_api/models/transfer_event_list_response.py` |

### client.transfer_event_sync

- **Route**: `POST /transfer/event/sync`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_event_sync(body: TransferEventSyncRequest | TransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferEventSyncResponse`
- **Returns (raw)**: `ApiResult[TransferEventSyncResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferEventSyncRequest` | `the_plaid_api/models/transfer_event_sync_request.py` |
| `TransferEventSyncRequestDict` | `the_plaid_api/models/transfer_event_sync_request.py` |
| `TransferEventSyncResponse` | `the_plaid_api/models/transfer_event_sync_response.py` |

### client.transfer_get

- **Route**: `POST /transfer/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_get(body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferGetResponse`
- **Returns (raw)**: `ApiResult[TransferGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferGetRequest` | `the_plaid_api/models/transfer_get_request.py` |
| `TransferGetRequestDict` | `the_plaid_api/models/transfer_get_request.py` |
| `TransferGetResponse` | `the_plaid_api/models/transfer_get_response.py` |

### client.transfer_intent_create

- **Route**: `POST /transfer/intent/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_intent_create(body: TransferIntentCreateRequest | TransferIntentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferIntentCreateResponse`
- **Returns (raw)**: `ApiResult[TransferIntentCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferIntentCreateRequest` | `the_plaid_api/models/transfer_intent_create_request.py` |
| `TransferIntentCreateRequestDict` | `the_plaid_api/models/transfer_intent_create_request.py` |
| `TransferIntentCreateResponse` | `the_plaid_api/models/transfer_intent_create_response.py` |

### client.transfer_intent_get

- **Route**: `POST /transfer/intent/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_intent_get(body: TransferIntentGetRequest | TransferIntentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferIntentGetResponse`
- **Returns (raw)**: `ApiResult[TransferIntentGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferIntentGetRequest` | `the_plaid_api/models/transfer_intent_get_request.py` |
| `TransferIntentGetRequestDict` | `the_plaid_api/models/transfer_intent_get_request.py` |
| `TransferIntentGetResponse` | `the_plaid_api/models/transfer_intent_get_response.py` |

### client.transfer_ledger_deposit

- **Route**: `POST /transfer/ledger/deposit`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_ledger_deposit(body: TransferLedgerDepositRequest | TransferLedgerDepositRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferLedgerDepositResponse`
- **Returns (raw)**: `ApiResult[TransferLedgerDepositResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferLedgerDepositRequest` | `the_plaid_api/models/transfer_ledger_deposit_request.py` |
| `TransferLedgerDepositRequestDict` | `the_plaid_api/models/transfer_ledger_deposit_request.py` |
| `TransferLedgerDepositResponse` | `the_plaid_api/models/transfer_ledger_deposit_response.py` |

### client.transfer_ledger_distribute

- **Route**: `POST /transfer/ledger/distribute`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_ledger_distribute(body: TransferLedgerDistributeRequest | TransferLedgerDistributeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferLedgerDistributeResponse`
- **Returns (raw)**: `ApiResult[TransferLedgerDistributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferLedgerDistributeRequest` | `the_plaid_api/models/transfer_ledger_distribute_request.py` |
| `TransferLedgerDistributeRequestDict` | `the_plaid_api/models/transfer_ledger_distribute_request.py` |
| `TransferLedgerDistributeResponse` | `the_plaid_api/models/transfer_ledger_distribute_response.py` |

### client.transfer_ledger_event_list

- **Route**: `POST /transfer/ledger/event/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_ledger_event_list(body: TransferLedgerEventListRequest | TransferLedgerEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferLedgerEventListResponse`
- **Returns (raw)**: `ApiResult[TransferLedgerEventListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferLedgerEventListRequest` | `the_plaid_api/models/transfer_ledger_event_list_request.py` |
| `TransferLedgerEventListRequestDict` | `the_plaid_api/models/transfer_ledger_event_list_request.py` |
| `TransferLedgerEventListResponse` | `the_plaid_api/models/transfer_ledger_event_list_response.py` |

### client.transfer_ledger_get

- **Route**: `POST /transfer/ledger/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_ledger_get(body: TransferLedgerGetRequest | TransferLedgerGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferLedgerGetResponse`
- **Returns (raw)**: `ApiResult[TransferLedgerGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferLedgerGetRequest` | `the_plaid_api/models/transfer_ledger_get_request.py` |
| `TransferLedgerGetRequestDict` | `the_plaid_api/models/transfer_ledger_get_request.py` |
| `TransferLedgerGetResponse` | `the_plaid_api/models/transfer_ledger_get_response.py` |

### client.transfer_ledger_withdraw

- **Route**: `POST /transfer/ledger/withdraw`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_ledger_withdraw(body: TransferLedgerWithdrawRequest | TransferLedgerWithdrawRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferLedgerWithdrawResponse`
- **Returns (raw)**: `ApiResult[TransferLedgerWithdrawResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferLedgerWithdrawRequest` | `the_plaid_api/models/transfer_ledger_withdraw_request.py` |
| `TransferLedgerWithdrawRequestDict` | `the_plaid_api/models/transfer_ledger_withdraw_request.py` |
| `TransferLedgerWithdrawResponse` | `the_plaid_api/models/transfer_ledger_withdraw_response.py` |

### client.transfer_list

- **Route**: `POST /transfer/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_list(body: TransferListRequest | TransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferListResponse`
- **Returns (raw)**: `ApiResult[TransferListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferListRequest` | `the_plaid_api/models/transfer_list_request.py` |
| `TransferListRequestDict` | `the_plaid_api/models/transfer_list_request.py` |
| `TransferListResponse` | `the_plaid_api/models/transfer_list_response.py` |

### client.transfer_metrics_get

- **Route**: `POST /transfer/metrics/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_metrics_get(body: TransferMetricsGetRequest | TransferMetricsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferMetricsGetResponse`
- **Returns (raw)**: `ApiResult[TransferMetricsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferMetricsGetRequest` | `the_plaid_api/models/transfer_metrics_get_request.py` |
| `TransferMetricsGetRequestDict` | `the_plaid_api/models/transfer_metrics_get_request.py` |
| `TransferMetricsGetResponse` | `the_plaid_api/models/transfer_metrics_get_response.py` |

### client.transfer_migrate_account

- **Route**: `POST /transfer/migrate_account`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_migrate_account(body: TransferMigrateAccountRequest | TransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferMigrateAccountResponse`
- **Returns (raw)**: `ApiResult[TransferMigrateAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferMigrateAccountRequest` | `the_plaid_api/models/transfer_migrate_account_request.py` |
| `TransferMigrateAccountRequestDict` | `the_plaid_api/models/transfer_migrate_account_request.py` |
| `TransferMigrateAccountResponse` | `the_plaid_api/models/transfer_migrate_account_response.py` |

### client.transfer_originator_create

- **Route**: `POST /transfer/originator/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_originator_create(body: TransferOriginatorCreateRequest | TransferOriginatorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferOriginatorCreateResponse`
- **Returns (raw)**: `ApiResult[TransferOriginatorCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferOriginatorCreateRequest` | `the_plaid_api/models/transfer_originator_create_request.py` |
| `TransferOriginatorCreateRequestDict` | `the_plaid_api/models/transfer_originator_create_request.py` |
| `TransferOriginatorCreateResponse` | `the_plaid_api/models/transfer_originator_create_response.py` |

### client.transfer_originator_funding_account_create

- **Route**: `POST /transfer/originator/funding_account/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_originator_funding_account_create(body: TransferOriginatorFundingAccountCreateRequest | TransferOriginatorFundingAccountCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferOriginatorFundingAccountCreateResponse`
- **Returns (raw)**: `ApiResult[TransferOriginatorFundingAccountCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferOriginatorFundingAccountCreateRequest` | `the_plaid_api/models/transfer_originator_funding_account_create_request.py` |
| `TransferOriginatorFundingAccountCreateRequestDict` | `the_plaid_api/models/transfer_originator_funding_account_create_request.py` |
| `TransferOriginatorFundingAccountCreateResponse` | `the_plaid_api/models/transfer_originator_funding_account_create_response.py` |

### client.transfer_originator_funding_account_update

- **Route**: `POST /transfer/originator/funding_account/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_originator_funding_account_update(body: TransferOriginatorFundingAccountUpdateRequest | TransferOriginatorFundingAccountUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferOriginatorFundingAccountUpdateResponse`
- **Returns (raw)**: `ApiResult[TransferOriginatorFundingAccountUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferOriginatorFundingAccountUpdateRequest` | `the_plaid_api/models/transfer_originator_funding_account_update_request.py` |
| `TransferOriginatorFundingAccountUpdateRequestDict` | `the_plaid_api/models/transfer_originator_funding_account_update_request.py` |
| `TransferOriginatorFundingAccountUpdateResponse` | `the_plaid_api/models/transfer_originator_funding_account_update_response.py` |

### client.transfer_originator_get

- **Route**: `POST /transfer/originator/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_originator_get(body: TransferOriginatorGetRequest | TransferOriginatorGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferOriginatorGetResponse`
- **Returns (raw)**: `ApiResult[TransferOriginatorGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferOriginatorGetRequest` | `the_plaid_api/models/transfer_originator_get_request.py` |
| `TransferOriginatorGetRequestDict` | `the_plaid_api/models/transfer_originator_get_request.py` |
| `TransferOriginatorGetResponse` | `the_plaid_api/models/transfer_originator_get_response.py` |

### client.transfer_originator_list

- **Route**: `POST /transfer/originator/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_originator_list(body: TransferOriginatorListRequest | TransferOriginatorListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferOriginatorListResponse`
- **Returns (raw)**: `ApiResult[TransferOriginatorListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferOriginatorListRequest` | `the_plaid_api/models/transfer_originator_list_request.py` |
| `TransferOriginatorListRequestDict` | `the_plaid_api/models/transfer_originator_list_request.py` |
| `TransferOriginatorListResponse` | `the_plaid_api/models/transfer_originator_list_response.py` |

### client.transfer_platform_originator_create

- **Route**: `POST /transfer/platform/originator/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_platform_originator_create(body: TransferPlatformOriginatorCreateRequest | TransferPlatformOriginatorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferPlatformOriginatorCreateResponse`
- **Returns (raw)**: `ApiResult[TransferPlatformOriginatorCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferPlatformOriginatorCreateRequest` | `the_plaid_api/models/transfer_platform_originator_create_request.py` |
| `TransferPlatformOriginatorCreateRequestDict` | `the_plaid_api/models/transfer_platform_originator_create_request.py` |
| `TransferPlatformOriginatorCreateResponse` | `the_plaid_api/models/transfer_platform_originator_create_response.py` |

### client.transfer_platform_person_create

- **Route**: `POST /transfer/platform/person/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_platform_person_create(body: TransferPlatformPersonCreateRequest | TransferPlatformPersonCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferPlatformPersonCreateResponse`
- **Returns (raw)**: `ApiResult[TransferPlatformPersonCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferPlatformPersonCreateRequest` | `the_plaid_api/models/transfer_platform_person_create_request.py` |
| `TransferPlatformPersonCreateRequestDict` | `the_plaid_api/models/transfer_platform_person_create_request.py` |
| `TransferPlatformPersonCreateResponse` | `the_plaid_api/models/transfer_platform_person_create_response.py` |

### client.transfer_platform_requirement_submit

- **Route**: `POST /transfer/platform/requirement/submit`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_platform_requirement_submit(body: TransferPlatformRequirementSubmitRequest | TransferPlatformRequirementSubmitRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferPlatformRequirementSubmitResponse`
- **Returns (raw)**: `ApiResult[TransferPlatformRequirementSubmitResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferPlatformRequirementSubmitRequest` | `the_plaid_api/models/transfer_platform_requirement_submit_request.py` |
| `TransferPlatformRequirementSubmitRequestDict` | `the_plaid_api/models/transfer_platform_requirement_submit_request.py` |
| `TransferPlatformRequirementSubmitResponse` | `the_plaid_api/models/transfer_platform_requirement_submit_response.py` |

### client.transfer_questionnaire_create

- **Route**: `POST /transfer/questionnaire/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_questionnaire_create(body: TransferQuestionnaireCreateRequest | TransferQuestionnaireCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferQuestionnaireCreateResponse`
- **Returns (raw)**: `ApiResult[TransferQuestionnaireCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferQuestionnaireCreateRequest` | `the_plaid_api/models/transfer_questionnaire_create_request.py` |
| `TransferQuestionnaireCreateRequestDict` | `the_plaid_api/models/transfer_questionnaire_create_request.py` |
| `TransferQuestionnaireCreateResponse` | `the_plaid_api/models/transfer_questionnaire_create_response.py` |

### client.transfer_recurring_cancel

- **Route**: `POST /transfer/recurring/cancel`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_recurring_cancel(body: TransferRecurringCancelRequest | TransferRecurringCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRecurringCancelResponse`
- **Returns (raw)**: `ApiResult[TransferRecurringCancelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRecurringCancelRequest` | `the_plaid_api/models/transfer_recurring_cancel_request.py` |
| `TransferRecurringCancelRequestDict` | `the_plaid_api/models/transfer_recurring_cancel_request.py` |
| `TransferRecurringCancelResponse` | `the_plaid_api/models/transfer_recurring_cancel_response.py` |

### client.transfer_recurring_create

- **Route**: `POST /transfer/recurring/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_recurring_create(body: TransferRecurringCreateRequest | TransferRecurringCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRecurringCreateResponse`
- **Returns (raw)**: `ApiResult[TransferRecurringCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRecurringCreateRequest` | `the_plaid_api/models/transfer_recurring_create_request.py` |
| `TransferRecurringCreateRequestDict` | `the_plaid_api/models/transfer_recurring_create_request.py` |
| `TransferRecurringCreateResponse` | `the_plaid_api/models/transfer_recurring_create_response.py` |

### client.transfer_recurring_get

- **Route**: `POST /transfer/recurring/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_recurring_get(body: TransferRecurringGetRequest | TransferRecurringGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRecurringGetResponse`
- **Returns (raw)**: `ApiResult[TransferRecurringGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRecurringGetRequest` | `the_plaid_api/models/transfer_recurring_get_request.py` |
| `TransferRecurringGetRequestDict` | `the_plaid_api/models/transfer_recurring_get_request.py` |
| `TransferRecurringGetResponse` | `the_plaid_api/models/transfer_recurring_get_response.py` |

### client.transfer_recurring_list

- **Route**: `POST /transfer/recurring/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_recurring_list(body: TransferRecurringListRequest | TransferRecurringListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRecurringListResponse`
- **Returns (raw)**: `ApiResult[TransferRecurringListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRecurringListRequest` | `the_plaid_api/models/transfer_recurring_list_request.py` |
| `TransferRecurringListRequestDict` | `the_plaid_api/models/transfer_recurring_list_request.py` |
| `TransferRecurringListResponse` | `the_plaid_api/models/transfer_recurring_list_response.py` |

### client.transfer_refund_cancel

- **Route**: `POST /transfer/refund/cancel`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_refund_cancel(body: TransferRefundCancelRequest | TransferRefundCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRefundCancelResponse`
- **Returns (raw)**: `ApiResult[TransferRefundCancelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRefundCancelRequest` | `the_plaid_api/models/transfer_refund_cancel_request.py` |
| `TransferRefundCancelRequestDict` | `the_plaid_api/models/transfer_refund_cancel_request.py` |
| `TransferRefundCancelResponse` | `the_plaid_api/models/transfer_refund_cancel_response.py` |

### client.transfer_refund_create

- **Route**: `POST /transfer/refund/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_refund_create(body: TransferRefundCreateRequest | TransferRefundCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRefundCreateResponse`
- **Returns (raw)**: `ApiResult[TransferRefundCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRefundCreateRequest` | `the_plaid_api/models/transfer_refund_create_request.py` |
| `TransferRefundCreateRequestDict` | `the_plaid_api/models/transfer_refund_create_request.py` |
| `TransferRefundCreateResponse` | `the_plaid_api/models/transfer_refund_create_response.py` |

### client.transfer_refund_get

- **Route**: `POST /transfer/refund/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_refund_get(body: TransferRefundGetRequest | TransferRefundGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRefundGetResponse`
- **Returns (raw)**: `ApiResult[TransferRefundGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRefundGetRequest` | `the_plaid_api/models/transfer_refund_get_request.py` |
| `TransferRefundGetRequestDict` | `the_plaid_api/models/transfer_refund_get_request.py` |
| `TransferRefundGetResponse` | `the_plaid_api/models/transfer_refund_get_response.py` |

### client.transfer_repayment_list

- **Route**: `POST /transfer/repayment/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_repayment_list(body: TransferRepaymentListRequest | TransferRepaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRepaymentListResponse`
- **Returns (raw)**: `ApiResult[TransferRepaymentListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRepaymentListRequest` | `the_plaid_api/models/transfer_repayment_list_request.py` |
| `TransferRepaymentListRequestDict` | `the_plaid_api/models/transfer_repayment_list_request.py` |
| `TransferRepaymentListResponse` | `the_plaid_api/models/transfer_repayment_list_response.py` |

### client.transfer_repayment_return_list

- **Route**: `POST /transfer/repayment/return/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_repayment_return_list(body: TransferRepaymentReturnListRequest | TransferRepaymentReturnListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRepaymentReturnListResponse`
- **Returns (raw)**: `ApiResult[TransferRepaymentReturnListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferRepaymentReturnListRequest` | `the_plaid_api/models/transfer_repayment_return_list_request.py` |
| `TransferRepaymentReturnListRequestDict` | `the_plaid_api/models/transfer_repayment_return_list_request.py` |
| `TransferRepaymentReturnListResponse` | `the_plaid_api/models/transfer_repayment_return_list_response.py` |

### client.transfer_return_recover

- **Route**: `POST /transfer/return/recover`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_return_recover(body: TransferReturnRecoverRequest | TransferReturnRecoverRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferReturnRecoverResponse`
- **Returns (raw)**: `ApiResult[TransferReturnRecoverResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferReturnRecoverRequest` | `the_plaid_api/models/transfer_return_recover_request.py` |
| `TransferReturnRecoverRequestDict` | `the_plaid_api/models/transfer_return_recover_request.py` |
| `TransferReturnRecoverResponse` | `the_plaid_api/models/transfer_return_recover_response.py` |

### client.transfer_sweep_get

- **Route**: `POST /transfer/sweep/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_sweep_get(body: TransferSweepGetRequest | TransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferSweepGetResponse`
- **Returns (raw)**: `ApiResult[TransferSweepGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferSweepGetRequest` | `the_plaid_api/models/transfer_sweep_get_request.py` |
| `TransferSweepGetRequestDict` | `the_plaid_api/models/transfer_sweep_get_request.py` |
| `TransferSweepGetResponse` | `the_plaid_api/models/transfer_sweep_get_response.py` |

### client.transfer_sweep_list

- **Route**: `POST /transfer/sweep/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def transfer_sweep_list(body: TransferSweepListRequest | TransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferSweepListResponse`
- **Returns (raw)**: `ApiResult[TransferSweepListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferSweepListRequest` | `the_plaid_api/models/transfer_sweep_list_request.py` |
| `TransferSweepListRequestDict` | `the_plaid_api/models/transfer_sweep_list_request.py` |
| `TransferSweepListResponse` | `the_plaid_api/models/transfer_sweep_list_response.py` |

### client.user_account_session_event_send

- **Route**: `POST /user_account/session/event/send`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_account_session_event_send(body: UserAccountSessionEventSendRequest | UserAccountSessionEventSendRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserAccountSessionEventSendResponse`
- **Returns (raw)**: `ApiResult[UserAccountSessionEventSendResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserAccountSessionEventSendRequest` | `the_plaid_api/models/user_account_session_event_send_request.py` |
| `UserAccountSessionEventSendRequestDict` | `the_plaid_api/models/user_account_session_event_send_request.py` |
| `UserAccountSessionEventSendResponse` | `the_plaid_api/models/user_account_session_event_send_response.py` |

### client.user_account_session_get

- **Route**: `POST /user_account/session/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_account_session_get(body: UserAccountSessionGetRequest | UserAccountSessionGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserAccountSessionGetResponse`
- **Returns (raw)**: `ApiResult[UserAccountSessionGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserAccountSessionGetRequest` | `the_plaid_api/models/user_account_session_get_request.py` |
| `UserAccountSessionGetRequestDict` | `the_plaid_api/models/user_account_session_get_request.py` |
| `UserAccountSessionGetResponse` | `the_plaid_api/models/user_account_session_get_response.py` |

### client.user_create

- **Route**: `POST /user/create`
- **Auth**: (`client_id` AND `secret` AND `plaid_version`) OR `oauth2`
- **Server**: `default`
- **Signature**: `def user_create(body: UserCreateRequest | UserCreateRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `plaid_new_user_api_enabled` — header `Plaid-New-User-API-Enabled` · `body` — JSON body
- **Returns (parsed)**: `UserCreateResponse`
- **Returns (raw)**: `ApiResult[UserCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserCreateRequest` | `the_plaid_api/models/user_create_request.py` |
| `UserCreateRequestDict` | `the_plaid_api/models/user_create_request.py` |
| `UserCreateResponse` | `the_plaid_api/models/user_create_response.py` |

### client.user_financial_data_refresh

- **Route**: `POST /user/financial_data/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_financial_data_refresh(body: UserFinancialDataRefreshRequest | UserFinancialDataRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserFinancialDataRefreshResponse`
- **Returns (raw)**: `ApiResult[UserFinancialDataRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserFinancialDataRefreshRequest` | `the_plaid_api/models/user_financial_data_refresh_request.py` |
| `UserFinancialDataRefreshRequestDict` | `the_plaid_api/models/user_financial_data_refresh_request.py` |
| `UserFinancialDataRefreshResponse` | `the_plaid_api/models/user_financial_data_refresh_response.py` |

### client.user_get

- **Route**: `POST /user/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_get(body: UserGetRequest | UserGetRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `plaid_new_user_api_enabled` — header `Plaid-New-User-API-Enabled` · `body` — JSON body
- **Returns (parsed)**: `UserGetResponse`
- **Returns (raw)**: `ApiResult[UserGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserGetRequest` | `the_plaid_api/models/user_get_request.py` |
| `UserGetRequestDict` | `the_plaid_api/models/user_get_request.py` |
| `UserGetResponse` | `the_plaid_api/models/user_get_response.py` |

### client.user_identity_remove

- **Route**: `POST /user/identity/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_identity_remove(body: UserIdentityRemoveRequest | UserIdentityRemoveRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `plaid_new_user_api_enabled` — header `Plaid-New-User-API-Enabled` · `body` — JSON body
- **Returns (parsed)**: `UserIdentityRemoveResponse`
- **Returns (raw)**: `ApiResult[UserIdentityRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserIdentityRemoveRequest` | `the_plaid_api/models/user_identity_remove_request.py` |
| `UserIdentityRemoveRequestDict` | `the_plaid_api/models/user_identity_remove_request.py` |
| `UserIdentityRemoveResponse` | `the_plaid_api/models/user_identity_remove_response.py` |

### client.user_items_associate

- **Route**: `POST /user/items/associate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_items_associate(body: UserItemsAssociateRequest | UserItemsAssociateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserItemsAssociateResponse`
- **Returns (raw)**: `ApiResult[UserItemsAssociateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserItemsAssociateRequest` | `the_plaid_api/models/user_items_associate_request.py` |
| `UserItemsAssociateRequestDict` | `the_plaid_api/models/user_items_associate_request.py` |
| `UserItemsAssociateResponse` | `the_plaid_api/models/user_items_associate_response.py` |

### client.user_items_get

- **Route**: `POST /user/items/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_items_get(body: UserItemsGetRequest | UserItemsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserItemsGetResponse`
- **Returns (raw)**: `ApiResult[UserItemsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserItemsGetRequest` | `the_plaid_api/models/user_items_get_request.py` |
| `UserItemsGetRequestDict` | `the_plaid_api/models/user_items_get_request.py` |
| `UserItemsGetResponse` | `the_plaid_api/models/user_items_get_response.py` |

### client.user_items_remove

- **Route**: `POST /user/items/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_items_remove(body: UserItemsRemoveRequest | UserItemsRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserItemsRemoveResponse`
- **Returns (raw)**: `ApiResult[UserItemsRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserItemsRemoveRequest` | `the_plaid_api/models/user_items_remove_request.py` |
| `UserItemsRemoveRequestDict` | `the_plaid_api/models/user_items_remove_request.py` |
| `UserItemsRemoveResponse` | `the_plaid_api/models/user_items_remove_response.py` |

### client.user_products_terminate

- **Route**: `POST /user/products/terminate`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_products_terminate(body: UserProductsTerminateRequest | UserProductsTerminateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserProductsTerminateResponse`
- **Returns (raw)**: `ApiResult[UserProductsTerminateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserProductsTerminateRequest` | `the_plaid_api/models/user_products_terminate_request.py` |
| `UserProductsTerminateRequestDict` | `the_plaid_api/models/user_products_terminate_request.py` |
| `UserProductsTerminateResponse` | `the_plaid_api/models/user_products_terminate_response.py` |

### client.user_remove

- **Route**: `POST /user/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_remove(body: UserRemoveRequest | UserRemoveRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `plaid_new_user_api_enabled` — header `Plaid-New-User-API-Enabled` · `body` — JSON body
- **Returns (parsed)**: `UserRemoveResponse`
- **Returns (raw)**: `ApiResult[UserRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserRemoveRequest` | `the_plaid_api/models/user_remove_request.py` |
| `UserRemoveRequestDict` | `the_plaid_api/models/user_remove_request.py` |
| `UserRemoveResponse` | `the_plaid_api/models/user_remove_response.py` |

### client.user_third_party_token_create

- **Route**: `POST /user/third_party_token/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_third_party_token_create(body: UserThirdPartyTokenCreateRequest | UserThirdPartyTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserThirdPartyTokenCreateResponse`
- **Returns (raw)**: `ApiResult[UserThirdPartyTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserThirdPartyTokenCreateRequest` | `the_plaid_api/models/user_third_party_token_create_request.py` |
| `UserThirdPartyTokenCreateRequestDict` | `the_plaid_api/models/user_third_party_token_create_request.py` |
| `UserThirdPartyTokenCreateResponse` | `the_plaid_api/models/user_third_party_token_create_response.py` |

### client.user_third_party_token_remove

- **Route**: `POST /user/third_party_token/remove`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_third_party_token_remove(body: UserThirdPartyTokenRemoveRequest | UserThirdPartyTokenRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserThirdPartyTokenRemoveResponse`
- **Returns (raw)**: `ApiResult[UserThirdPartyTokenRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserThirdPartyTokenRemoveRequest` | `the_plaid_api/models/user_third_party_token_remove_request.py` |
| `UserThirdPartyTokenRemoveRequestDict` | `the_plaid_api/models/user_third_party_token_remove_request.py` |
| `UserThirdPartyTokenRemoveResponse` | `the_plaid_api/models/user_third_party_token_remove_response.py` |

### client.user_transactions_refresh

- **Route**: `POST /user/transactions/refresh`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_transactions_refresh(body: UserTransactionsRefreshRequest | UserTransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserTransactionsRefreshResponse`
- **Returns (raw)**: `ApiResult[UserTransactionsRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserTransactionsRefreshRequest` | `the_plaid_api/models/user_transactions_refresh_request.py` |
| `UserTransactionsRefreshRequestDict` | `the_plaid_api/models/user_transactions_refresh_request.py` |
| `UserTransactionsRefreshResponse` | `the_plaid_api/models/user_transactions_refresh_response.py` |

### client.user_update

- **Route**: `POST /user/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def user_update(body: UserUpdateRequest | UserUpdateRequestDict, *, plaid_new_user_api_enabled: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `plaid_new_user_api_enabled` — header `Plaid-New-User-API-Enabled` · `body` — JSON body
- **Returns (parsed)**: `UserUpdateResponse`
- **Returns (raw)**: `ApiResult[UserUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserUpdateRequest` | `the_plaid_api/models/user_update_request.py` |
| `UserUpdateRequestDict` | `the_plaid_api/models/user_update_request.py` |
| `UserUpdateResponse` | `the_plaid_api/models/user_update_response.py` |

### client.wallet_create

- **Route**: `POST /wallet/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def wallet_create(body: WalletCreateRequest | WalletCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletCreateResponse`
- **Returns (raw)**: `ApiResult[WalletCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WalletCreateRequest` | `the_plaid_api/models/wallet_create_request.py` |
| `WalletCreateRequestDict` | `the_plaid_api/models/wallet_create_request.py` |
| `WalletCreateResponse` | `the_plaid_api/models/wallet_create_response.py` |

### client.wallet_get

- **Route**: `POST /wallet/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def wallet_get(body: WalletGetRequest | WalletGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletGetResponse`
- **Returns (raw)**: `ApiResult[WalletGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WalletGetRequest` | `the_plaid_api/models/wallet_get_request.py` |
| `WalletGetRequestDict` | `the_plaid_api/models/wallet_get_request.py` |
| `WalletGetResponse` | `the_plaid_api/models/wallet_get_response.py` |

### client.wallet_list

- **Route**: `POST /wallet/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def wallet_list(body: WalletListRequest | WalletListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletListResponse`
- **Returns (raw)**: `ApiResult[WalletListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WalletListRequest` | `the_plaid_api/models/wallet_list_request.py` |
| `WalletListRequestDict` | `the_plaid_api/models/wallet_list_request.py` |
| `WalletListResponse` | `the_plaid_api/models/wallet_list_response.py` |

### client.wallet_transaction_execute

- **Route**: `POST /wallet/transaction/execute`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def wallet_transaction_execute(body: WalletTransactionExecuteRequest | WalletTransactionExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletTransactionExecuteResponse`
- **Returns (raw)**: `ApiResult[WalletTransactionExecuteResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WalletTransactionExecuteRequest` | `the_plaid_api/models/wallet_transaction_execute_request.py` |
| `WalletTransactionExecuteRequestDict` | `the_plaid_api/models/wallet_transaction_execute_request.py` |
| `WalletTransactionExecuteResponse` | `the_plaid_api/models/wallet_transaction_execute_response.py` |

### client.wallet_transaction_get

- **Route**: `POST /wallet/transaction/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def wallet_transaction_get(body: WalletTransactionGetRequest | WalletTransactionGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletTransactionGetResponse`
- **Returns (raw)**: `ApiResult[WalletTransactionGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WalletTransactionGetRequest` | `the_plaid_api/models/wallet_transaction_get_request.py` |
| `WalletTransactionGetRequestDict` | `the_plaid_api/models/wallet_transaction_get_request.py` |
| `WalletTransactionGetResponse` | `the_plaid_api/models/wallet_transaction_get_response.py` |

### client.wallet_transaction_list

- **Route**: `POST /wallet/transaction/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def wallet_transaction_list(body: WalletTransactionListRequest | WalletTransactionListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WalletTransactionListResponse`
- **Returns (raw)**: `ApiResult[WalletTransactionListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WalletTransactionListRequest` | `the_plaid_api/models/wallet_transaction_list_request.py` |
| `WalletTransactionListRequestDict` | `the_plaid_api/models/wallet_transaction_list_request.py` |
| `WalletTransactionListResponse` | `the_plaid_api/models/wallet_transaction_list_response.py` |

### client.watchlist_screening_entity_create

- **Route**: `POST /watchlist_screening/entity/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_create(body: WatchlistScreeningEntityCreateRequest | WatchlistScreeningEntityCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityCreateResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityCreateRequest` | `the_plaid_api/models/watchlist_screening_entity_create_request.py` |
| `WatchlistScreeningEntityCreateRequestDict` | `the_plaid_api/models/watchlist_screening_entity_create_request.py` |
| `WatchlistScreeningEntityCreateResponse` | `the_plaid_api/models/watchlist_screening_entity_create_response.py` |

### client.watchlist_screening_entity_get

- **Route**: `POST /watchlist_screening/entity/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_get(body: WatchlistScreeningEntityGetRequest | WatchlistScreeningEntityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityGetResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityGetRequest` | `the_plaid_api/models/watchlist_screening_entity_get_request.py` |
| `WatchlistScreeningEntityGetRequestDict` | `the_plaid_api/models/watchlist_screening_entity_get_request.py` |
| `WatchlistScreeningEntityGetResponse` | `the_plaid_api/models/watchlist_screening_entity_get_response.py` |

### client.watchlist_screening_entity_history_list

- **Route**: `POST /watchlist_screening/entity/history/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_history_list(body: WatchlistScreeningEntityHistoryListRequest | WatchlistScreeningEntityHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityHistoryListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityHistoryListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityHistoryListRequest` | `the_plaid_api/models/watchlist_screening_entity_history_list_request.py` |
| `WatchlistScreeningEntityHistoryListRequestDict` | `the_plaid_api/models/watchlist_screening_entity_history_list_request.py` |
| `WatchlistScreeningEntityHistoryListResponse` | `the_plaid_api/models/watchlist_screening_entity_history_list_response.py` |

### client.watchlist_screening_entity_hit_list

- **Route**: `POST /watchlist_screening/entity/hit/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_hit_list(body: WatchlistScreeningEntityHitListRequest | WatchlistScreeningEntityHitListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityHitListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityHitListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityHitListRequest` | `the_plaid_api/models/watchlist_screening_entity_hit_list_request.py` |
| `WatchlistScreeningEntityHitListRequestDict` | `the_plaid_api/models/watchlist_screening_entity_hit_list_request.py` |
| `WatchlistScreeningEntityHitListResponse` | `the_plaid_api/models/watchlist_screening_entity_hit_list_response.py` |

### client.watchlist_screening_entity_list

- **Route**: `POST /watchlist_screening/entity/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_list(body: WatchlistScreeningEntityListRequest | WatchlistScreeningEntityListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityListRequest` | `the_plaid_api/models/watchlist_screening_entity_list_request.py` |
| `WatchlistScreeningEntityListRequestDict` | `the_plaid_api/models/watchlist_screening_entity_list_request.py` |
| `WatchlistScreeningEntityListResponse` | `the_plaid_api/models/watchlist_screening_entity_list_response.py` |

### client.watchlist_screening_entity_program_get

- **Route**: `POST /watchlist_screening/entity/program/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_program_get(body: WatchlistScreeningEntityProgramGetRequest | WatchlistScreeningEntityProgramGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityProgramGetResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityProgramGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityProgramGetRequest` | `the_plaid_api/models/watchlist_screening_entity_program_get_request.py` |
| `WatchlistScreeningEntityProgramGetRequestDict` | `the_plaid_api/models/watchlist_screening_entity_program_get_request.py` |
| `WatchlistScreeningEntityProgramGetResponse` | `the_plaid_api/models/watchlist_screening_entity_program_get_response.py` |

### client.watchlist_screening_entity_program_list

- **Route**: `POST /watchlist_screening/entity/program/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_program_list(body: WatchlistScreeningEntityProgramListRequest | WatchlistScreeningEntityProgramListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityProgramListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityProgramListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityProgramListRequest` | `the_plaid_api/models/watchlist_screening_entity_program_list_request.py` |
| `WatchlistScreeningEntityProgramListRequestDict` | `the_plaid_api/models/watchlist_screening_entity_program_list_request.py` |
| `WatchlistScreeningEntityProgramListResponse` | `the_plaid_api/models/watchlist_screening_entity_program_list_response.py` |

### client.watchlist_screening_entity_review_create

- **Route**: `POST /watchlist_screening/entity/review/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_review_create(body: WatchlistScreeningEntityReviewCreateRequest | WatchlistScreeningEntityReviewCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityReviewCreateResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityReviewCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityReviewCreateRequest` | `the_plaid_api/models/watchlist_screening_entity_review_create_request.py` |
| `WatchlistScreeningEntityReviewCreateRequestDict` | `the_plaid_api/models/watchlist_screening_entity_review_create_request.py` |
| `WatchlistScreeningEntityReviewCreateResponse` | `the_plaid_api/models/watchlist_screening_entity_review_create_response.py` |

### client.watchlist_screening_entity_review_list

- **Route**: `POST /watchlist_screening/entity/review/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_review_list(body: WatchlistScreeningEntityReviewListRequest | WatchlistScreeningEntityReviewListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityReviewListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityReviewListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityReviewListRequest` | `the_plaid_api/models/watchlist_screening_entity_review_list_request.py` |
| `WatchlistScreeningEntityReviewListRequestDict` | `the_plaid_api/models/watchlist_screening_entity_review_list_request.py` |
| `WatchlistScreeningEntityReviewListResponse` | `the_plaid_api/models/watchlist_screening_entity_review_list_response.py` |

### client.watchlist_screening_entity_update

- **Route**: `POST /watchlist_screening/entity/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_entity_update(body: WatchlistScreeningEntityUpdateRequest | WatchlistScreeningEntityUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningEntityUpdateResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningEntityUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningEntityUpdateRequest` | `the_plaid_api/models/watchlist_screening_entity_update_request.py` |
| `WatchlistScreeningEntityUpdateRequestDict` | `the_plaid_api/models/watchlist_screening_entity_update_request.py` |
| `WatchlistScreeningEntityUpdateResponse` | `the_plaid_api/models/watchlist_screening_entity_update_response.py` |

### client.watchlist_screening_individual_create

- **Route**: `POST /watchlist_screening/individual/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_create(body: WatchlistScreeningIndividualCreateRequest | WatchlistScreeningIndividualCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualCreateResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualCreateRequest` | `the_plaid_api/models/watchlist_screening_individual_create_request.py` |
| `WatchlistScreeningIndividualCreateRequestDict` | `the_plaid_api/models/watchlist_screening_individual_create_request.py` |
| `WatchlistScreeningIndividualCreateResponse` | `the_plaid_api/models/watchlist_screening_individual_create_response.py` |

### client.watchlist_screening_individual_get

- **Route**: `POST /watchlist_screening/individual/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_get(body: WatchlistScreeningIndividualGetRequest | WatchlistScreeningIndividualGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualGetResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualGetRequest` | `the_plaid_api/models/watchlist_screening_individual_get_request.py` |
| `WatchlistScreeningIndividualGetRequestDict` | `the_plaid_api/models/watchlist_screening_individual_get_request.py` |
| `WatchlistScreeningIndividualGetResponse` | `the_plaid_api/models/watchlist_screening_individual_get_response.py` |

### client.watchlist_screening_individual_history_list

- **Route**: `POST /watchlist_screening/individual/history/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_history_list(body: WatchlistScreeningIndividualHistoryListRequest | WatchlistScreeningIndividualHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualHistoryListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualHistoryListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualHistoryListRequest` | `the_plaid_api/models/watchlist_screening_individual_history_list_request.py` |
| `WatchlistScreeningIndividualHistoryListRequestDict` | `the_plaid_api/models/watchlist_screening_individual_history_list_request.py` |
| `WatchlistScreeningIndividualHistoryListResponse` | `the_plaid_api/models/watchlist_screening_individual_history_list_response.py` |

### client.watchlist_screening_individual_hit_list

- **Route**: `POST /watchlist_screening/individual/hit/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_hit_list(body: WatchlistScreeningIndividualHitListRequest | WatchlistScreeningIndividualHitListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualHitListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualHitListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualHitListRequest` | `the_plaid_api/models/watchlist_screening_individual_hit_list_request.py` |
| `WatchlistScreeningIndividualHitListRequestDict` | `the_plaid_api/models/watchlist_screening_individual_hit_list_request.py` |
| `WatchlistScreeningIndividualHitListResponse` | `the_plaid_api/models/watchlist_screening_individual_hit_list_response.py` |

### client.watchlist_screening_individual_list

- **Route**: `POST /watchlist_screening/individual/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_list(body: WatchlistScreeningIndividualListRequest | WatchlistScreeningIndividualListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualListRequest` | `the_plaid_api/models/watchlist_screening_individual_list_request.py` |
| `WatchlistScreeningIndividualListRequestDict` | `the_plaid_api/models/watchlist_screening_individual_list_request.py` |
| `WatchlistScreeningIndividualListResponse` | `the_plaid_api/models/watchlist_screening_individual_list_response.py` |

### client.watchlist_screening_individual_program_get

- **Route**: `POST /watchlist_screening/individual/program/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_program_get(body: WatchlistScreeningIndividualProgramGetRequest | WatchlistScreeningIndividualProgramGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualProgramGetResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualProgramGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualProgramGetRequest` | `the_plaid_api/models/watchlist_screening_individual_program_get_request.py` |
| `WatchlistScreeningIndividualProgramGetRequestDict` | `the_plaid_api/models/watchlist_screening_individual_program_get_request.py` |
| `WatchlistScreeningIndividualProgramGetResponse` | `the_plaid_api/models/watchlist_screening_individual_program_get_response.py` |

### client.watchlist_screening_individual_program_list

- **Route**: `POST /watchlist_screening/individual/program/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_program_list(body: WatchlistScreeningIndividualProgramListRequest | WatchlistScreeningIndividualProgramListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualProgramListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualProgramListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualProgramListRequest` | `the_plaid_api/models/watchlist_screening_individual_program_list_request.py` |
| `WatchlistScreeningIndividualProgramListRequestDict` | `the_plaid_api/models/watchlist_screening_individual_program_list_request.py` |
| `WatchlistScreeningIndividualProgramListResponse` | `the_plaid_api/models/watchlist_screening_individual_program_list_response.py` |

### client.watchlist_screening_individual_review_create

- **Route**: `POST /watchlist_screening/individual/review/create`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_review_create(body: WatchlistScreeningIndividualReviewCreateRequest | WatchlistScreeningIndividualReviewCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualReviewCreateResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualReviewCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualReviewCreateRequest` | `the_plaid_api/models/watchlist_screening_individual_review_create_request.py` |
| `WatchlistScreeningIndividualReviewCreateRequestDict` | `the_plaid_api/models/watchlist_screening_individual_review_create_request.py` |
| `WatchlistScreeningIndividualReviewCreateResponse` | `the_plaid_api/models/watchlist_screening_individual_review_create_response.py` |

### client.watchlist_screening_individual_review_list

- **Route**: `POST /watchlist_screening/individual/review/list`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_review_list(body: WatchlistScreeningIndividualReviewListRequest | WatchlistScreeningIndividualReviewListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualReviewListResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualReviewListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualReviewListRequest` | `the_plaid_api/models/watchlist_screening_individual_review_list_request.py` |
| `WatchlistScreeningIndividualReviewListRequestDict` | `the_plaid_api/models/watchlist_screening_individual_review_list_request.py` |
| `WatchlistScreeningIndividualReviewListResponse` | `the_plaid_api/models/watchlist_screening_individual_review_list_response.py` |

### client.watchlist_screening_individual_update

- **Route**: `POST /watchlist_screening/individual/update`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def watchlist_screening_individual_update(body: WatchlistScreeningIndividualUpdateRequest | WatchlistScreeningIndividualUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WatchlistScreeningIndividualUpdateResponse`
- **Returns (raw)**: `ApiResult[WatchlistScreeningIndividualUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WatchlistScreeningIndividualUpdateRequest` | `the_plaid_api/models/watchlist_screening_individual_update_request.py` |
| `WatchlistScreeningIndividualUpdateRequestDict` | `the_plaid_api/models/watchlist_screening_individual_update_request.py` |
| `WatchlistScreeningIndividualUpdateResponse` | `the_plaid_api/models/watchlist_screening_individual_update_response.py` |

### client.webhook_verification_key_get

- **Route**: `POST /webhook_verification_key/get`
- **Auth**: `client_id` AND `secret` AND `plaid_version`
- **Server**: `default`
- **Signature**: `def webhook_verification_key_get(body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WebhookVerificationKeyGetResponse`
- **Returns (raw)**: `ApiResult[WebhookVerificationKeyGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WebhookVerificationKeyGetRequest` | `the_plaid_api/models/webhook_verification_key_get_request.py` |
| `WebhookVerificationKeyGetRequestDict` | `the_plaid_api/models/webhook_verification_key_get_request.py` |
| `WebhookVerificationKeyGetResponse` | `the_plaid_api/models/webhook_verification_key_get_response.py` |

