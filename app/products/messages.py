from common.provider import CleanCodeMessage


class ProductsMessages:
    PRODUCT_NOT_FOUND = CleanCodeMessage("E001", "Product not found")
    PRODUCT_CREATE_FAILED = CleanCodeMessage("E002", "Can not create product")
    PRODUCT_UPDATE_FAILED = CleanCodeMessage("E003", "Can not update product")
    PRODUCT_DELETE_FAILED = CleanCodeMessage("E004", "Can not delete product")
