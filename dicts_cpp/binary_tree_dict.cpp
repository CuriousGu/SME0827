#include <string>
#include <iostream>

using namespace std;


class BinaryTreeDict{

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

    public:
        BinaryTreeDict() : root(nullptr) {}

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
    };





// int main(){
//     BinaryTreeDict a;

//     a["primeiro"] = "gustavo";
//     a["primeiro"] = "fernanda";

//     cout << a["primeiro"] << endl;

//     return 0;
// }