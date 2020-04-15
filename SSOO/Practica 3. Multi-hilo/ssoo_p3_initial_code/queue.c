


#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include "queue.h"


//queue *q = (queue *)malloc(size*sizeof(struct element));

//To create a queue
queue* queue_init(int size){
    ring = malloc(size*sizeof(struct element));
    queue * q = (queue *)malloc(sizeof(queue));
    q->size = size;
    q->length = 0;
    q->head = 0;
    q->tail = 0;
    return q;
}

// To Enqueue an element, head se inserta y tail salen.
int queue_put(queue *q, struct element* x) {
  if (q.queue_full == 0){
    q->ring[q->head] = x;
    q->head = (q->head+1) % q->size;
    q-> length = q->length + 1;
    return 0;
  }
  return -1;
}


// To Dequeue an element.
struct element* queue_get(queue *q) {
  if (q.queue_empty == 0){
      struct element *elem;
      elem = q->ring[q->tail];
      q->tail= (q->tail+1) % q->size;
      q->length = q->length - 1;
      return elem;
  }
  return NULL;
}


//To check queue state
int queue_empty(queue *q){
    if(q->length==0)
      return 1;
    return 0;
}

int queue_full(queue *q){
    if (q->length == q->size)
      return 1;
    return 0;
}

//To destroy the queue and free the resources
int queue_destroy(queue *q){
  free(q->ring);
  free(q);
  return 0;
}