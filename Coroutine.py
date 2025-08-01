def print_name(prefix):
    print(f"Searching prefix: {prefix}")
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")

# Instantiate and start the coroutine
corou = print_name("Come")
corou.__next__()

# Send values to the coroutine
corou.send("Come back Thank You")
corou.send("Thank you")

# Close the coroutine
corou.close()