#   mydata=   [
#         {
#                    'grn_id': 'GRN-1', 
#                    'receipt_id': 'TD-1', 
#                    'client': '32201-123456',
#                    'item': 'MAZ', 
#                    'gross_weight': 10.11, 
#                    'net_weight': 10.0,
#                    'deduction': 10, 
#                    'moisture': 1, 
#                    'grade': '1',
#                    'price_per_tonne': 20000.0,
#                    'total_commodity_price': 200000.0, 
#                    'total_payable_price': 210000.0, 
#                    'transaction_fees': 0.0,
#                    'transaction_type': 'Trade',
#                    'is_received_at_warehouse': True, 
#                    'bags': 10, 
#                    'warehouse': 'SOB', 
#                    'truck_no': 'SOXDER 234B',
#                    'total_deduction': 10,
#                    'raised_for_farmer': True, 
#                    'qr_code': [200000, 29993], 
#                    'loan_id': 'LN-12345677',
#                    'created_offline': '2020-10-12T03:36:08.08+0100'
#                    },
                
#                   {
#                    'grn_id': 'GRN-1', 
#                    'receipt_id': 'TD-1', 
#                    'client': '32201-123456',
#                    'item': 'MAZ', 
#                    'gross_weight': 10.11, 
#                    'net_weight': 10.0,
#                    'deduction': 10, 
#                    'moisture': 1, 
#                    'grade': '1',
#                    'price_per_tonne': 20000.0,
#                    'total_commodity_price': 200000.0, 
#                    'total_payable_price': 210000.0, 
#                    'transaction_fees': 0.0,
#                    'transaction_type': 'Trade',
#                    'is_received_at_warehouse': True, 
#                    'bags': 10, 
#                    'warehouse': 'SOB', 
#                    'truck_no': 'SOXDER 234B',
#                    'total_deduction': 10,
#                    'raised_for_farmer': False, 
#                    'qr_code': [323232, 12121], 
#                    'loan_id': 'LN-12345677',
#                    'created_offline': '2020-10-12T03:36:08.08+0100'
#                    },
                  
#                     {
#                    'grn_id': 'GRN-1', 
#                    'receipt_id': 'TD-1', 
#                    'client': '32201-123456',
#                    'item': 'MAZ', 
#                    'gross_weight': 10.11, 
#                    'net_weight': 10.0,
#                    'deduction': 10, 
#                    'moisture': 1, 
#                    'grade': '1',
#                    'price_per_tonne': 20000.0,
#                    'total_commodity_price': 200000.0, 
#                    'total_payable_price': 210000.0, 
#                    'transaction_fees': 0.0,
#                    'transaction_type': 'Trade',
#                    'is_received_at_warehouse': True, 
#                    'bags': 10, 
#                    'warehouse': 'SOMB', 
#                    'truck_no': 'SOXDER 234B',
#                    'total_deduction': 10,
#                    'raised_for_farmer': False, 
#                    'qr_code': [2111111, 920001], 
#                    'loan_id': 'LN-2qw32',
#                    'created_offline': '2020-10-12T03:36:08.08+0100'
#                    }
#          ]
#     all_apilog = APIRequestLogging.objects.filter(
#         view='/WB3/api/v1/goods_receipt_line').count()
#     sold_more_than_five = {}
#     for c in mydata:
#         if c["qr_code"] == False:
#             sold_more_than_five[c["warehouse"]] = c["client"]
#             print(sold_more_than_five)
#     print(all_apilog)
#     print('lss')
#     context = {'unsynced_grn_error_number':all_apilog, }
    
#     return render(request, 'account/sysadmin_dashboard.html', context)
