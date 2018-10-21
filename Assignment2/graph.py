class Graph{

    public main_list adj;   

    public Graph(){
        adj = new main_list();
    }

    public void addEdge(Node a, Node b, int weight){
        int search1=0,search2=0;
        list_node temp = adj.head;

        if(temp==null){
            list p = new list(new Node(a.vertex));
            b.weight = weight;
            p.insert(b);
            this.adj.insert((new list_node(p)));

            if(a.compare(b)==1){
                return;
            }
            else{
                list q = new list(new Node(b.vertex));
                b.weigth=weight;
                q.insert(b);
                this.adj.insert(new list_node(q));
            }
            return;

        }

        while(temp.next!=null){
            if(temp.data.head.compare(a)==1){
                temp.data.insert(b);
                search=1;
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
    public int vertex,weight;
    public int color = -1;
    public Node next=null;

    public Node(int a, int b){
        vertex = a;
        weight = b;
        next = null;
    }

    public Node(int a){
        vertex=a;
        weight=0;
        next=null;
    }

    // public int compare(Node b){
    //     if(this.vertex==b.vertex && this.weight==b.team2){
    //         return 1;
    //     }
    //     return 0;   
    // }


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