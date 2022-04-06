from pydantic import BaseModel


class VNPayIn(BaseModel):
    vn_amount: int
    order_info: str


class VNPayReturnIn(BaseModel):
    vnp_Amount: int
    vnp_BankCode: str
    vnp_BankTranNo: int
    vnp_CardType: str
    vnp_OrderInfo: str
    vnp_PayDate: str
    vnp_ResponseCode: str
    vnp_TmnCode: str
    vnp_TransactionNo: str
    vnp_TransactionStatus: str
    vnp_TxnRef: str
    vnp_SecureHash: str
