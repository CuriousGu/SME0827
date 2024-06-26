#ifndef BINARY_TREE_H
#define BINARY_TREE_H

#include <string>
#include <iostream>

using namespace std;


class BinaryTree{

    private:
        class Node{
            public:
                Node* left; 
                Node* right;
                string key; 
                string value;

                Node(string valor, string chave): 
                    key(chave), value(valor), left(nullptr), right(nullptr) {}
        };

        Node* root;
        unsigned int _size = 0;

        Node* min(Node* node){
            Node* curr = node;
            while(curr && curr->left != nullptr){
                curr = curr->left;
            }
            return curr;
        }

        Node* remove(Node* node, string key){
            if(!(node)){
                return node;
            }

            if(key < node->key){
                node->left = remove(node->left, key);
            }
            else if(key > node->key){
                node->right = remove(node->right, key);
            }
            else{
                if(!(node->left) || !(node->right)){
                    if(node->left){
                        return node->left;
                    }
                    else{
                        return node->right;
                    }
                }
                else{
                    Node* temp = min(node->right);
                    node->key = temp->key;
                    node->value = temp->value;
                    node->right = remove(node->right, temp->key);
                }
            }
            return node;
        }


    public:
        BinaryTree() : root(nullptr) {}

        unsigned int size(){
            return _size;
        }

        string& insert(Node*& node, const string& key){
            if(!(node)){
                node = new Node(" ", key);
                _size++;
                return node->value;
            }

            Node* pointer = node;
            while(pointer){
                if(key < pointer->key){
                    if(pointer->left){
                        pointer = pointer->left;
                    }
                    else{
                        pointer->left = new Node(" ", key);
                        _size++;
                        break;
                    }
                }
                else if(key > pointer->key){
                    if(pointer->right){
                        pointer = pointer->right;
                    }
                    else{
                        pointer->right = new Node(" ", key);
                        _size++;
                        break;
                    }
                }
                else{
                    break;
                }
            }
            return node->value;
        }

        // sobrecarga do operador. Para simular a 
        // implementação do python -> dict['a'] = 'b'
        string& operator[](const string& key) {
            return insert(root, key);
        }

        void pop(string key){
            root = remove(root, key);
            if(_size > 0){_size--;}
        }
    };

#endif // BINARY_TREE_H
