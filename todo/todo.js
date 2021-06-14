const input = document.querySelector('.todos-input');
const button = document.querySelector('.todos-button');
const todosContainer = document.querySelector('.todos');
const deleteButton = document.querySelector('.delete-button');

const DeleteButton = () => {
    let _deleteButton = document.createElement('button');
    _deleteButton.appendChild(document.createTextNode("X"));
    _deleteButton.classList.add('delete-button');

    return _deleteButton
}

const Todo = (value) => {
    let _todo = document.createElement('li');
    _todo.appendChild(document.createTextNode(value));
    _todo.appendChild(DeleteButton());

    return _todo;
}

button.addEventListener('click', () => {
    const value = input.value;
    if (value.split(' ').join('') == '')
        return;

    todosContainer.appendChild(Todo(value));
    input.value = '';
});

document.addEventListener('click', (e) => {
    if (e.target.classList[0] == 'delete-button') {
        const todo = e.target.parentElement;
        todosContainer.removeChild(todo);
    }
});