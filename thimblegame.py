import random

class ThimbleGame:
    def __init__(self, num_buckets=3):
        self.num_buckets = num_buckets
        self.ball_position = None
        self.buckets = [{'visible': True, 'has_ball': False} for _ in range(num_buckets)]
        self.hide_ball()

    def hide_ball(self):
        """Randomly hide the ball in one bucket (invisible logic)"""
        ball_index = random.randint(0, self.num_buckets - 1)
        for i, bucket in enumerate(self.buckets):
            bucket['has_ball'] = (i == ball_index)

    def make_bucket_invisible(self, bucket_number):
        """Make a specific bucket invisible during gameplay"""
        if 0 <= bucket_number < self.num_buckets:
            self.buckets[bucket_number]['visible'] = False

    def make_bucket_visible(self, bucket_number):
        """Make a bucket visible again"""
        if 0 <= bucket_number < self.num_buckets:
            
            self.buckets[bucket_number]['visible'] = True

    def display_buckets(self):
        """Show only visible buckets"""
        print("\nVisible Buckets:")
        for i, bucket in enumerate(self.buckets):
            if bucket['visible']:
                print(f"  Bucket {i + 1}: Visible")
            else:
                print(f"  Bucket {i + 1}: [INVISIBLE]")

    def guess(self, bucket_number):
        """Check if guess is correct"""
        if not self.buckets[bucket_number - 1]['visible']:
            return "Cannot guess an invisible bucket!"
        return self.buckets[bucket_number - 1]['has_ball']

def play_thimble_game():
    """Main game loop for interactive thimble game"""
    print("=" * 50)
    print("        WELCOME TO THE THIMBLE GAME!")
    print("=" * 50)
    
    score = 0
    
    while True:
        game = ThimbleGame(3)
        
        print("\n🎮 A new round begins!")
        print("A ball is hidden under one of 3 buckets...")
        input("Press Enter to continue...")
        
        # Hide 1 random bucket
        invisible_bucket = random.randint(0, 2)
        game.make_bucket_invisible(invisible_bucket)
        print(f"\n✨ One bucket mysteriously disappears...")
        
        # Display visible buckets
        game.display_buckets()
        
        # Get player's guess
        while True:
            try:
                guess = int(input("\n🤔 Which bucket do you think has the ball? (1-3): "))
                if guess < 1 or guess > 3:
                    print("❌ Please enter 1, 2, or 3!")
                    continue
                break
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        # Check guess
        result = game.guess(guess)
        
        if isinstance(result, str):  # Error message (invisible bucket)
            print(f"\n⚠️  {result}")
            continue
        
        # Reveal result
        print("\n" + "=" * 50)
        if result:
            print("🎉 YOU WIN! The ball was under bucket {}!".format(guess))
            score += 1
        else:
            # Show where the ball actually was
            for i, bucket in enumerate(game.buckets):
                if bucket['has_ball']:
                    print("❌ WRONG! The ball was under bucket {}!".format(i + 1))
                    break
        
        print(f"📊 Score: {score}")
        print("=" * 50)
        
        # Ask to play again
        play_again = input("\nPlay again? (yes/no): ").lower().strip()
        if play_again != 'yes' and play_again != 'y':
            print(f"\n🏆 Final Score: {score}")
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_thimble_game()