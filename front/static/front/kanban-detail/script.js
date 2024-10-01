document.addEventListener('DOMContentLoaded', () => {
    // Inicializa o sortable em cada lista de tarefas
    document.querySelectorAll('.task-list').forEach((list) => {
        new Sortable(list, {
            group: 'tasks',
            animation: 150,
            onEnd: (evt) => {
                const taskId = evt.item.getAttribute('data-task-id');
                const newColumnPosition = evt.to.closest('.kanban-column').getAttribute('data-column-position'); // Obtém a posição da nova coluna

                // Envia a requisição para atualizar a posição da tarefa
                fetch(`/api/task/${taskId}/change_task_position/`, {
                    method: 'PATCH',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken(),
                    },
                    body: JSON.stringify({
                        position: newColumnPosition, // Envia a nova posição da coluna
                    }),
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        // Tarefa movida com sucesso
                        console.log("Task moved successfully!");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            },
        });
    });

    // Manipula a visibilidade do formulário de adicionar coluna
    const addColumnButton = document.getElementById('add-column-button');
    const addColumnForm = document.getElementById('add-column-form');
    const cancelButton = document.getElementById('cancel-column-button');

    addColumnButton.addEventListener('click', () => {
        addColumnForm.style.display = 'block'; // Exibe o formulário
    });

    cancelButton.addEventListener('click', () => {
        addColumnForm.style.display = 'none'; // Oculta o formulário
    });

    // Manipula o envio do formulário para adicionar uma nova coluna
    document.getElementById('new-column-form').addEventListener('submit', (event) => {
        event.preventDefault();

        const columnName = document.getElementById('column-name').value;
        const todoId = document.getElementById('todo-id').value;

        fetch('/api/column/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({
                name: columnName,
                todo: todoId,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                // Recarregue a página ou adicione a nova coluna dinamicamente
                location.reload();
            }
        });
    });
});

// Função para obter o CSRF token do meta tag
function getCsrfToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}
