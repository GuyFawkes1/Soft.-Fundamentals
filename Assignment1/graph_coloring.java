public class graph_coloring{

    public static void main(String[] args){

        graph_coloring g = new graph_coloring();
        int n=200;
        Graph G = g.graph_creation(n);
        //G.print_graph();
        list[] colored_graph = g.coloring(n*n-n,G);
        list temp = colored_graph[1];
        int i=1;
        while(temp!=null){
            
            Node temp2 = temp.head;
            while(temp2!=null){
                System.out.print("("+temp2.team1+","+temp2.team2+")"+";");
                temp2 = temp2.next;
            }
            System.out.println();
            System.out.println();
            i = i+1;
            temp = colored_graph[i];
        }
    }


    //n is total number of matches
    public list[] coloring(int n,Graph G){
        list[] colored = new list[n+1];


        int i=0,vertices=0,color=0;
        while(vertices<n){

            color = color+1;
            colored[color] = new list();
            list_node temp = G.adj.head;
            while(temp!=null){
                if(temp.data.head.color==-1){
                    Node temp2 = temp.data.head.next;
                    while(temp2!=null){
                        if(colored[color].Search(temp2)){
                            break;
                        }
                        temp2=temp2.next;
                    }
                    if(temp2==null){
                        temp.data.head.color=color;
                        colored[color].insert(temp.data.head);
                        vertices++;
                    }
                    
                }
                temp = temp.next;
            }
            
                
            }
            return colored;

            
        }




    public Graph graph_creation(int v){
        Graph G1 = new Graph();
        for(int i=1;i<v+1;i++){
            for(int j =1;j<v+1;j++){
                if(i!=j){
                    Node temp1 = new Node(i,j);
                    for(int k=1;k<v+1;k++){
                        if(k!=i){
                            Node temp2 = new Node(i,k);
                            G1.addEdge(temp1,temp2);
                            
                            temp2 = new Node(k,i);
                            G1.addEdge(temp1,temp2);
                        }
                        if(k!=j){    
                            Node temp3 = new Node(j,k);
                            G1.addEdge(temp1,temp3);
                            
                            temp3 = new Node(k,j);
                            G1.addEdge(temp1,temp3);
                        }
                    }
                    
                }
            }
        }
        return G1;

    }

}



class Graph{

    public main_list adj;   

    public Graph(){
        adj = new main_list();
    }

    public void addEdge(Node a, Node b){
        int search1=0,search2=0;
        list_node temp = adj.head; 
        if(temp == null){
            list p = new list(new Node(a.team1,a.team2));
            p.insert(new Node(b.team1,b.team2));
            this.adj.insert(new list_node(p));

            if(a.compare(b)==1){
                return;}
            else{
            list q = new list(new Node(b.team1,b.team2));
            q.insert(new Node(a.team1,a.team2));
            
            this.adj.insert(new list_node(q));
            }
            // this.print_graph();
            // System.out.println("Ohbgvfcd");
            return;
        }
        while(temp.next!=null){
            // System.out.print("d1");
            if(temp.data.head.compare(a)==1){
                temp.data.insert(b);
                search1=1;
            }
            if(temp.data.head.compare(b)==1){
                temp.data.insert(a);
                search2=1;   
            }
            temp = temp.next;   
        }

        if(search1==0){
            if(temp.data.head.compare(a)==1){
                temp.data.insert(b);
            }
            else{
                list p = new list(a);
                p.insert(b);
                this.adj.insert(new list_node(p));
            }
        }

        if(search2==0){
            if(temp.data.head.compare(b)==1){
                temp.data.insert(a);
            }
            else{
                list q = new list(b);
                q.insert(a);
                this.adj.insert(new list_node(q));
            }
        }
    }

        //Prints the entire graph for debugging purposes

        public void print_graph(){
            list_node temp = adj.head;
            while(temp!=null){
                System.out.print("("+temp.data.head.team1+","+temp.data.head.team2+"),");
                Node temp2 = temp.data.head.next;
                while(temp2!=null){
                    System.out.print("("+temp2.team1+","+temp2.team2+")");
                    temp2 = temp2.next;
                }
                System.out.println();
                temp = temp.next;
            }
        }
}


//An element in main_list is the list of vertices that have an edge with the head of that list

class main_list{
    public list_node head;
    public main_list(){
        this.head=null;
    }
    public main_list(list_node h){
        this.head=h;
    }



    public void insert(list_node h){
        list_node temp = this.head;
        if(temp!=null)
        {
            while(temp.next!=null){
                // System.out.print("d3");
            temp = temp.next;
            }
        temp.next = new list_node(h.data);
        }
        else{
            head = new list_node(h.data);
        }

    }

}


class list{
    public Node head;
    public list(){
        this.head=null;
    }
    public list(Node h){
        this.head=h;
    }

    public boolean Search(Node key){
        Node temp = this.head;
        while(temp!=null){
            if(temp.compare(key)==1){
                return true;
            }
            temp = temp.next;
        }
        return false;
    }

    //inserts a Node into the list if an identical one doesn't exist in the list

    public void insert(Node h){
        Node temp = this.head;
        if(temp!=null)
        {
            while(temp.next!=null){
                // System.out.print("d4");
                if(temp.compare(h)==1){
                    return;
                }
                temp = temp.next;
            }
            if(temp.compare(h)==1){
                    return;
                }
            temp.next = new Node(h.team1,h.team2);
        }
        else{
            head = new Node(h.team1,h.team2);
        }

    }

}


//Node is the building block of the list that contains vertices

class Node{
    public int team1,team2;
    public int color = -1;
    public Node next=null;

    public Node(int a, int b){
        team1 = a;
        team2 = b;
        next = null;
    }

    public int compare(Node b){
        if(this.team1==b.team1 && this.team2==b.team2){
            return 1;
        }
        return 0;   
    }


}


//list_node is the building block of the list that corresponds to the vertex to which the adjacency list is made

class list_node{

    public list data;
    public list_node next;
    public list_node(){
        this.data = null;
        next=null;
    }
    public list_node(list data){
        this.data = data;
        next=null;
    }

}