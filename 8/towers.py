def do_towers(n,start,intermediate,end):
    if n == 1:
        print ("Disk 1 from",start,"to",end)
    else:
        do_towers(n-1,start,end,intermediate)
        print ("Disk",n,"from",start,"to",end)
        do_towers(n-1,intermediate,start,end)
