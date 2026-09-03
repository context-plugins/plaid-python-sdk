from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_credit_funds_source import TransferCreditFundsSourceOrStr
from .enums.transfer_type import TransferTypeOrStr
from .transfer_user_in_response import TransferUserInResponse, TransferUserInResponseDict
from .transfer_wire_details import TransferWireDetails, TransferWireDetailsDict


class TransferAuthorizationProposedTransfer(SdkBaseModel):
    """Details regarding the proposed transfer."""

    ach_class: Optional[AchclassOrStr] = UNSET
    """Specifies the use case of the transfer. Required for transfers on an ACH network. For more details, see `ACH SEC
    codes <https://plaid.com/docs/transfer/creating-transfers/#ach-sec-codes>`__.

    Codes supported for credits: ``ccd``, ``ppd`` Codes supported for debits: ``ccd``, ``ppd``, ``tel``, ``web``

    ``"ccd"`` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    ``"ppd"`` - Prearranged Payment or Deposit - The transfer is part of a pre-existing relationship with a consumer.
    Authorization was obtained in writing either in person or via an electronic document signing, e.g. Docusign, by the
    consumer. Can be used for credits or debits.

    ``"web"`` - Internet-Initiated Entry. The transfer debits a consumer's bank account. Authorization from the consumer
    is obtained over the Internet (e.g. a web or mobile application). Can be used for single debits or recurring debits.

    ``"tel"`` - Telephone-Initiated Entry. The transfer debits a consumer. Debit authorization has been received orally
    over the telephone via a recorded call."""

    account_id: Optional[str] = UNSET
    """The Plaid ``account_id`` for the account that will be debited or credited."""

    funding_account_id: str | None
    """The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of
    your business checking accounts will be credited or debited."""

    ledger_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a Plaid Ledger Balance."""

    type_: TransferTypeOrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

    requested_amount: str
    """The amount originally requested by the client when creating the authorization (decimal string with two digits of
    precision e.g. "800.00"). This may differ from ``amount``, the amount Plaid proposes to transfer, when only a
    partial amount is offered as part of an Adaptive Guarantee."""

    network: str
    """The network or rails used for the transfer."""

    wire_details: OptionalNullable[TransferWireDetails] = UNSET
    """Information specific to wire transfers."""

    origination_account_id: str
    """Plaid's unique identifier for the origination account that was used for this transfer."""

    iso_currency_code: str
    """The currency of the transfer amount. The default value is "USD"."""

    originator_client_id: str | None
    """The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client
    as a `Platform customer <https://plaid.com/docs/transfer/application/#originators-vs-platforms>`__."""

    credit_funds_source: TransferCreditFundsSourceOrStr | None


class TransferAuthorizationProposedTransferDict(TypedDict):
    ach_class: NotRequired[AchclassOrStr]
    account_id: NotRequired[str]
    funding_account_id: str | None
    ledger_id: NotRequired[str | None]
    type_: TransferTypeOrStr
    user: TransferUserInResponse | TransferUserInResponseDict
    amount: str
    requested_amount: str
    network: str
    wire_details: NotRequired[TransferWireDetails | TransferWireDetailsDict | None]
    origination_account_id: str
    iso_currency_code: str
    originator_client_id: str | None
    credit_funds_source: TransferCreditFundsSourceOrStr | None
