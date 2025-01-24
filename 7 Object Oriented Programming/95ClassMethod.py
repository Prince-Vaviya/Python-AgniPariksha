class Counter:
    # Class variable
    count = 0

    @classmethod
    def increment_count(cls):
        """Increment the class variable count."""
        cls.count += 1

    @staticmethod
    def display_message():
        print("This is a utility message from the Counter class.")

def main():
    print(f"Initial count: {Counter.count}")

    # Increment the count
    Counter.increment_count()
    print(f"Count after incrementing: {Counter.count}")

    # Increment the count again
    Counter.increment_count()
    print(f"Count after another increment: {Counter.count}")

    # Display utility message
    Counter.display_message()


if __name__ == "__main__":
    main()