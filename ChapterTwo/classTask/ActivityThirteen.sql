SELECT SKU, SKU_Description, WarehouseID FROM inventory
WHERE QuantityOnHand > 1 and QuantityOnOrder < 10