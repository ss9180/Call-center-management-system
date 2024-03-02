#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 100

struct Queue{
    char items[MAX_SIZE];
    int front;
    int rear;
};

void initialize(struct Queue* queue) {
    queue->front = -1;
    queue->rear = -1;
}

bool is_empty(const struct Queue* queue) {
    return queue->front == -1;
}

bool is_full(const struct Queue* queue) {
    return (queue->rear + 1) % MAX_SIZE == queue->front;
}

void enqueue(struct Queue* queue, char item) {
    if (!is_full(queue)) {
        if (is_empty(queue)) {
            queue->front = 0;
        }
        queue->rear = (queue->rear + 1) % MAX_SIZE;
        queue->items[queue->rear] = item;
        printf("Enqueued: %c\n", item);
    } else {
        printf("Queue is full, cannot enqueue: %c\n", item);
    }
}

char dequeue(struct Queue* queue) {
    char item = ' ';
    if (!is_empty(queue)) {
        item = queue->items[queue->front];
        if (queue->front == queue->rear) {
            queue->front = queue->rear = -1;
        } else {
            queue->front = (queue->front + 1) % MAX_SIZE;
        }
        printf("Dequeued: %c\n", item);
    } else {
        printf("Queue is empty\n");
    }
    return item;
}

int main() {
    struct Queue queue;
    initialize(&queue);

    // Enqueue some calls
    enqueue(&queue, '1');
    enqueue(&queue, '2');

    // Simulate agent picking up calls
    printf("Agent 1 picks up %c\n", dequeue(&queue));
    printf("Agent 2 picks up %c\n", dequeue(&queue));

    // Simulate resolving calls
    printf("Call 1 is resolved\n");
    dequeue(&queue);
    printf("Call 2 is resolved\n");
    dequeue(&queue);

    // Check if the queue is empty
    if (is_empty(&queue)) {
        printf("Queue is empty\n");
    } else {
        printf("Queue is not empty\n");
    }

    return 0;
}