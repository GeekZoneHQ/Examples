# Switch between multiple while loops

run_mode = 0
barcode = 0
run_mode = 0

## main loop ##
while (run_mode <= 3):
    
    barcode = raw_input("\n\nInput: ")
    run_mode = int(barcode)
    
    while (run_mode == 1):
        print("Loop 1")
        print("Run Mode = " + str(run_mode))
        run_mode = 0

    while (run_mode == 2):
        print("Loop 2")
        print("Run Mode = " + str(run_mode))
        run_mode = 0

    while (run_mode == 3):
        print("Loop 3")
        print("Run Mode = " + str(run_mode))
        run_mode = 0
        

print("Done!")


