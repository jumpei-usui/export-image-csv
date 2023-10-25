from lambda_function import handler


if __name__ == "__main__":
    for i in range(1000):
        handler(event=f"{i}.png", context=None)
