# TEMITOPE WAREHOUSE CREATE
@login_required
@custom_permission_required(CAN_CREATE_WAREHOUSE_AUDIT)
def create_warehouse_audit_view2(request):
    tenant = request.user.tenant
    warehouse_code = request.GET.get('warehouse', '')
    print(warehouse_code)
    warehouse_item = request.POST.get('items')
    bag = request.POST.get('bag')
    weight = request.POST.get('weight')
    comment = request.POST.get('comment')
    grade = request.POST.get('grade')
    all_tenants_items= Item.objects.get_for_tenant(tenant)
    if request.method == 'POST':
        return HttpResponse('ll')
    if warehouse_code == "":
        return HttpResponse('error')
    elif warehouse_code and request.method == 'GET':
            warehouse_inventory = WarehouseInventoryAccount.objects. \
                filter(warehouse__code=warehouse_code, warehouse__tenant=tenant). \
                values('grade', 'item__product__name','item', 'warehouse', 'total_bags',
                    'total_net_weight').order_by('item')
    return render(request, 'audit/create_warehouse_audit.html', {'warehouses': Warehouse.objects.get_for_tenant(tenant),'warehouse_inventory':warehouse_inventory,'all_tenants_items':all_tenants_items})




