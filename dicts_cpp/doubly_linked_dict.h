#ifndef DOUBLY_LINKED_H
#define DOUBLY_LINKED_H

#include <string>
#include <iostream>

using namespace std;


class DoublyLinked{

    private:
        class Node{
            public:
                Node* next = nullptr;
                Node* prev = nullptr;
                string key;
                string value;

                Node(string valor, string chave, Node* anterior, Node* proximo): 
                    key(chave), value(valor), prev(anterior), next(proximo) {}
        };

        void del(string key){
            Node* curr = head;
            while(curr){
                if(curr->key == key){
                    if(curr->prev){
                        curr->prev->next = curr->next;
                    }
                    if(curr->next){
                        curr->next->prev = curr->prev;
                    }
                    if(curr == head){
                        head = curr->next;
                    }
                    if(curr == tail){
                        tail = curr->prev;
                    }
                    _size--;
                    return;
                }
                curr = curr->next;
            }
            throw runtime_error(key + "not found");
        }

        Node* head = nullptr;
        Node* tail = new Node(nullptr, nullptr, head, nullptr);
        unsigned int _size = 0;

    public:
        unsigned int size(){
            return _size;
        }

        string& insert(Node*& node, const string& key){
            if(!(node)){
                node = new Node(" ", key, nullptr, tail);
                _size++;
                return node->value;
            }
            else{
                Node* curr = head;
                while(curr){
                    if(key == curr->key){
                        return curr->value;
                    }
                    if(!(curr->next)){
                        break;
                    }
                    curr = curr->next;
                }
                _size++;
                Node* new_node = new Node("", key, nullptr, nullptr);
                tail->next = new_node;
                new_node->prev = tail;
                tail = new_node;

                return new_node->value;
            }
        }

        string& operator[](const string& key) {
            return insert(head, key);
        }

        void pop(string key = ""){
            if(_size == 0){
                throw runtime_error("Empty Dict");
            }
            if(key == ""){
                Node* item = tail;
                del(key);
                return;
            }
            else{
                Node* item = head;
                while(item){
                    if(item->key == key){
                        del(item->key);
                        return;
                    }
                    item = item->next;
                }
                throw runtime_error(key + "not found");
            }
        }
};

#endif // DOUBLY_LINKED_H
