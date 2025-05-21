SELECT SKU, SKU_Description, WarehouseID FROM inventory
WHERE QuantityOnHand = 0 and QuantityOnOrder > 0
order by WarehouseID desc, SKU asc