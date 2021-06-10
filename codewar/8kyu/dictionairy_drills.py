#def fillable(stock, merch, n):
#    if merch in stock:
#        if n > stock[merch]:
#            return False
#        else:
#           return True
#    else:
#        return False


def fillable(stock, merch, n):
    return stock.get(merch,0) >= n