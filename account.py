class Account:
    """
    Class that generates new instances of account credentials to be stored.
    """
    def __init__(self, acc_ty, acc_uname, acc_pass,acc_cpass):
        self.acc_ty = acc_ty
        self.acc_uname = acc_uname
        self.acc_pass = acc_pass
        self.acc_cpass = acc_cpass