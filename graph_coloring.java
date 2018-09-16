public class graph_coloring{

    public static void main(){

        graph_coloring g = new graph_coloring();
        Graph M = g.graph_creation(3);
        M.print_graph();


    }

    public Graph graph_creation(int v){
        Graph G1 = new graph();
        for(int i=1;i<V+1;i++){
            for(int j =0;j<V+1;j++){
                if(i!=j){
                    Node temp1 = new Node(i,j);
                    for(int k=0;k<V+1;k++){
                        if(k!=i){
                            Node temp2 = new Node(i,k);
                            G1.addEdge(temp1,temp2);
                            temp2 = new Node(k,i);
                            G1.addEdge(temp1,temp2);

                        }
                    }
                    
                }
            }
        }
        return G1;

    }

}

class Graph{

    public list<list_node> adj;   

    public graph(){
        adj = new list();
    }

    public void addEdge(Node a, Node b){
        int search1=0,search2=0;
        list_node temp = adj.head; 
        if(temp == null){
            list<Node> p = new list(a);
            p.insert(b);
            list<Node> q = new list(b);
            q.insert(a);
            this.adj.insert(new list_node(p));
            this.adj.insert(new list_node(q));
            return;
        }
        while(temp.next!=null){
            if(temp.data.head.compare(a)){
                temp.data.insert(b);
                search1=1;
            }
            if(temp.data.head.compare(b)){
                temp.data.insert(a);
                search2=1;   
            }
            temp = temp.next;
            
        }
        if(search1==0){
            list<Node> p = new list(a);
            p.insert(b);
            this.adj.insert(new list_node(p));
        }

        if(search2==0){
            list<Node> q = new list(b);
            q.insert(a);
            this.adj.insert(new list_node(q));
            
        }

        public void print_graph(){
            list<Node> temp = adj.head;
            while(temp!=null){
                System.out.println("("+temp.head.team1+","+temp.head.team2+")");
                Node temp2 = temp.head;
                while(temp2!=null){
                    System.out.println("("+temp2.team1+","+temp.head.team2+")");
                    temp2 = temp2.next;
                }
                temp = temp.next;
            }
        }
    }

    public addVertex(){

    }


}


class list_node{

    public list<Node> data;
    public list_node next;
    public list_node(){
        this.data = null;
        next=null;
    }
    public list_node(data){
        this.data = data;
        next=null;
    }

}


class list<E>{
    public E head;
    public list(){
        this.head=null;
    }
    public list(E h){
        this.head=h;
    }



    public insert(E h){
        E temp = this.head;
        if(temp!=null)
        {
            while(temp.next!=null){
            if(temp.compare(h)){
                return;
            }
            temp = temp.next;
            }
        temp.next = h;
        }
        else{
            head = h;
        }

    }

}

class Node{
    public int team1,team2;
    public int color = -1;
    public Node next;

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

