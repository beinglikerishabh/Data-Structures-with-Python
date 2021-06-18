def TOH(disknumber,startpeg=1,endpeg=3):
    if disknumber:
        TOH(disknumber-1,startpeg,6-startpeg-endpeg)
        print(f"move disk{disknumber} from peg{startpeg} to peg{endpeg}")
        TOH(disknumber-1,6-startpeg-endpeg,endpeg)

n = int(input("enter the number of disks"))
TOH(n)