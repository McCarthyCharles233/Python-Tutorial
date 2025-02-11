posts = []  # List to store posts

def create_post():
    title = input("Enter the title of the post: ")
    content = input("Enter the content of the post: ")

    post = {
        'title': title,
        'content': content,
    }

    posts.append(post)
    print("Post added successfully!")


def view_posts():
    if not posts:
        print("No posts available.")
    else:
        print("\nList of Posts:")
        for post in posts:
            print(f"Title: {post['title']}, Content: {post['content']}")


def find_post():
    title = input("Search the post by entering the title name: ").strip().lower()

    if not posts:
        print("No available posts.")
        return

    for post in posts:
        if post['title'].strip().lower() == title:
            print(f"Post found!\nTitle: {post['title']}, Content: {post['content']}")
            return

    print("Post not found.")


def delete_post():
    title = input("Enter the title of the post to delete: ").strip().lower()

    for post in posts:
        if post['title'].strip().lower() == title:
            posts.remove(post)
            print("Post deleted successfully!")
            return

    print("Post not found.")


create_post()
view_posts()
find_post()
delete_post()
view_posts()
