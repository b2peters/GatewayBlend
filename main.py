import requests
import json

def get_all_todos():
    resp=requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo_item in resp.json():
        print('id: {}\nuserId: {}\ntitle: {}\ncompleted: {}\n'.format(todo_item['id'], todo_item['userId'], todo_item['title'], todo_item['completed'],))


def find_by_id(id):
    resp = requests.get('https://jsonplaceholder.typicode.com/todos/'+id)
    todo_item = resp.json()
    print('id: {}\nuserId: {}\ntitle: {}\ncompleted: {}\n'.format(todo_item['id'], todo_item['userId'], todo_item['title'], todo_item['completed'],))   
    
def delete_by_id(id):
    return requests.delete('https://jsonplaceholder.typicode.com/todos/'+id)
    print(resp.status_code) 

def make_a_new_todo(title, userId):
    return requests.post('https://jsonplaceholder.typicode.com/todos', json={title:title, userId:userId})

if __name__ = "__main__":

    app.run()