document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.task-list').forEach((list) => {
        new Sortable(list, {
            group: 'tasks',
            animation: 150,
            onEnd: (evt) => {
                const taskId = evt.item.getAttribute('data-task-id');
                const columnId = evt.from.getAttribute('data-column-id');
                const newColumnPosition = Array.from(evt.from.parentNode.children).indexOf(evt.from) + 1; // Calcula a nova posição

                fetch(`/api/task/${taskId}/change_task_position/`, {
                    method: 'PATCH',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken()
                    },
                    body: JSON.stringify({
                        position: newColumnPosition // Envia a nova posição da coluna
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        // Tarefa movida com sucesso
                    }
                });
            }
        });
    });

    // Toggle the visibility of the add column form
    const addColumnButton = document.getElementById('add-column-button');
    const addColumnForm = document.getElementById('add-column-form');
    const cancelButton = document.getElementById('cancel-column-button');

    addColumnButton.addEventListener('click', () => {
        addColumnForm.classList.remove('hidden');
    });

    cancelButton.addEventListener('click', () => {
        addColumnForm.classList.add('hidden');
    });

    // Add new column form submission
    document.getElementById('new-column-form').addEventListener('submit', (event) => {
        event.preventDefault();

        const columnName = document.getElementById('column-name').value;
        const todoId = document.getElementById('todo-id').value;

        fetch('/api/column/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({
                name: columnName,
                todo: todoId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                // Reload the page or add the new column dynamically
                location.reload();
            }
        });
    });
});

// Function to get CSRF token from meta tag
function getCsrfToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}
