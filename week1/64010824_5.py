bid_input = (input("Enter All Bid : ").split())
bid = list(map(int,bid_input))

for x in range(len(bid)) :
    if len(bid) == 1 :
        print("not enough bidder")
    elif len(bid) > 1 :
        max_bid = max(bid)
        count_bid = bid.count(max_bid)
        if count_bid > 1 :
            print("error : have more than one highest bid")
            bid.clear()
        else :
            bid.sort() 
            print("winner bid is" ,max_bid ,"need to pay" ,bid[-2])
            bid.clear()