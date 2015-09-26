package general;

import java.util.ArrayList;

public class Rules {
	
	private enum ValoresDesicion {

	    ventaFuerte (0.5), //Separamos con comas

	    venta (1.5),

	    noHacerNada(3.5),

	    compra (4.5),

	    compraFuerte (1000);  

	    private final double limite;

	

	    ValoresDesicion (double pesoEspecifico) { 

	        this.limite = pesoEspecifico;

	    } 


	    public double limite() { return limite; }

	} 
	
	private enum ValoresDesicionParcial {

	    ventaFuerte (0), 
	    
	    venta (1),

	    noHacerNada(2),
	    
	    noActuar(3),

	    compra (4),

	    compraFuerte (5);  

	    private final int limite;

	

	    ValoresDesicionParcial (int pesoEspecifico) { 

	        this.limite = pesoEspecifico;

	    } 


	    public int limite() { return limite; }

	} 
	
	private ArrayList<Integer> ganaciaOperativa;
	private ArrayList<Integer>  valorGanado;
	private ArrayList<Integer>  roa;
	private ArrayList<Integer>  roe;
	private ArrayList<Integer>  valorDeLibro;
	private ArrayList<Integer>  efectoPalanca;
	
	private int ponderacionGanaciaOperativa;
	private int ponderacionValorGanado;
	private int ponderacionRoa;
	private int ponderacionRoe;
	private int ponderacionValorDeLibro;
	private int ponderacionEfectoPalanca;
	
	private ArrayList<String> valores;
	private ValoresDesicionParcial parciales;
	
	public Rules(ArrayList<Integer> go,ArrayList<Integer> vg,
			ArrayList<Integer> roa,ArrayList<Integer> roe, 
			ArrayList<Integer> vl,ArrayList<Integer> ep, double plazoEnMeses){
		
		this.efectoPalanca = new ArrayList<Integer>();
		this.valorGanado = new ArrayList<Integer>();
		this.roa = new ArrayList<Integer>();
		this.roe = new ArrayList<Integer>();
		this.valorDeLibro = new ArrayList<Integer>();
		this.ganaciaOperativa = new ArrayList<Integer>();
		
		for(int limite: go) this.ganaciaOperativa.add(limite);
		for(int limite: vg) this.valorGanado.add(limite);
		for(int limite: roa) this.roa.add(limite);
		for(int limite: roa) this.roe.add(limite);
		for(int limite: vl) this.valorDeLibro.add(limite);
		for(int limite: ep) this.efectoPalanca.add(limite);
		
		this.ponderacionGanaciaOperativa = (plazoEnMeses < 1.5)? 15 : 30;
		this.ponderacionValorGanado = (plazoEnMeses < 1.5)? 10 : 20;
		this.ponderacionRoa = (plazoEnMeses < 1.5)? 5 : 10;
		this.ponderacionRoe = (plazoEnMeses < 1.5)? 5 : 10;
		this.ponderacionValorDeLibro = (plazoEnMeses < 1.5)? 5 : 10;
		this.ponderacionEfectoPalanca = (plazoEnMeses < 1.5)? 5 : 10;
		
	}
	
	
	public ValoresDesicionParcial decisionRespectoGananciaOperativa(double porcentaje){
		int desicion = 0; 
		if(porcentaje < this.ganaciaOperativa.get(0))
			desicion = 0;
		else if ((porcentaje >= this.ganaciaOperativa.get(0)) && (porcentaje < this.ganaciaOperativa.get(1)))
			desicion = 1;
		else if ((porcentaje >= this.ganaciaOperativa.get(1)) && (porcentaje < this.ganaciaOperativa.get(2)))
			desicion = 2;
		else if ((porcentaje >= this.ganaciaOperativa.get(2)) && (porcentaje < this.ganaciaOperativa.get(3)))
			desicion = 3;
		else if ((porcentaje >= this.ganaciaOperativa.get(3)) && (porcentaje < this.ganaciaOperativa.get(4)))
			desicion = 4;
		else if (porcentaje >= this.ganaciaOperativa.get(4))
			desicion = 5;
		
		return this.parciales.values()[desicion];
	}
	
	
}
