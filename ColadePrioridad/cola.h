#ifndef COLAP_H
#define COLAP_H
#include "lista.h"

typedef<int> Elemento;

class colaPrioridad {
    Lista l;
    public:
        colaPrioridad();
        void enqueue(Elemento);
        void deque();
        Elemento front();
        bool empty();
}
#endif