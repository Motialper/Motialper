#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *ls, *rs;
} Node;

Node* newNode(int data) {
    Node *p = (Node*) malloc (sizeof(Node));
    p->data = data;
    p->ls = p->rs = NULL;
    return p;
}
void insert(Node (**root), int data) {
    if ((*root) == NULL)
        (*root) = newNode(data);
    else
        if (data > (*root)->data)
            insert(&(*root)->rs,data);
        else
            insert(&(*root)->ls,data);
}
int treeHeight(Node *root) {
    if (root == NULL)
        return 0;
    else{
        int maxR = treeHeight(root -> rs);
        int maxL = treeHeight(root -> ls);
        
        if (maxR > maxL)
            //printf("%d", maxR);
            return maxR + 1;
        else
            //printf("%d", maxL);
            return maxL + 1;
        
        }      
}
int numOfNodes(Node *root) {
    if (root == NULL)
        return 0;
    else{
        int numR = numOfNodes(root -> rs);
        int numL = numOfNodes(root -> ls);
        
        int sumNode = numR + numL;
        return sumNode + 1;
        
        }      
}
void printTreeRec(Node *root) {
    printf("the rec is %d\n" ,root->data);
}
void printTree(Node *root) {
    if (root == NULL)
        return;
    else 
        printTree(root->ls);
        printf("%d\n", root->data);
        printTree(root->rs);


}
void freeTree(Node *root) {
    if (root == NULL)
        return;
    freeTree(root->rs);
    freeTree(root->rs);
    freeTree(root);
}
int isIn(Node *root, int data) {
    if (root == NULL)
        return 0;
    if (root->data == data)
        return 1;
    if (root->data > data)
        isIn(root->ls, data);
    else       
        isIn(root->rs, data);
         

}

int main() {
    int array[] = {5,3,8,1,4,9,45,34};
    int N = sizeof(array)/sizeof(int);
    
    Node *root = NULL;
    int i;
    for(i=0; i<N; ++i)
        insert(&root,array[i]);
    printTree(root);
    for(i=1; i<=10; ++i)
        if(isIn(root,i))
        printf("%d is in the tree.\n",i);
    printf("Tree Height: %d\n", treeHeight(root));
    printTreeRec(root);

    printf("Number of nodes: %d \n", numOfNodes(root));
    freeTree(root);
    
    return 0;
    }
