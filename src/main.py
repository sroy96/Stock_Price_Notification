#!/usr/bin/python3
import sys
sys.path.append('/home/saurav/Documents/Personal_projects/market-notification/models/')
from models import user_stock_relation
from utils import cache_util

if __name__ == '__main__':
    cache_util.create_cache_client().flush_all()
    print(f"=============Hello Welcome to Stock Exchange notification Service===============")
    print(f"==============Please Provide stock details============================")
    cache_util.create_cache_client().flush_all()
    while True:
        user_email = input("please enter your email id: ")
        nse_code = input("enter stock code as on NSE Listing: ")
        target = input("provide target: ")
        stop_loss = input("notify stop loss at: ")
        set_percentage_margin = input("percent margin at: ")
        stock_exchange_name = input("nse or bse: ")
        print(f"THANKS FOR THE DETAILS WE WILL NOTIFY YOU !!")
        user_relation_obj = user_stock_relation.UserStocksRelation(user_email=user_email,
                                                                   stock_exchange_name=stock_exchange_name,
                                                                   nse_code=nse_code.upper(), target=target, stop_loss=stop_loss,
                                                                   set_percent_margin=set_percentage_margin)
        user_relation_obj.add_to_observer_queue()
