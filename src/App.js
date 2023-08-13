import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import { useEffect } from "react";
import { useState } from "react";

function App() {
  const [products, setProducts] = useState([]); // [
  // const response = fetch("https://hama-be.vercel.app/api/products")
  //   .then((res) => res.json())
  //   .then((res) => {
  //     console.log(res);
  //   });

// should 
  const getProducts = async () => {
    const response = await axios.get("https://hama-be.vercel.app/api/products");
    setProducts(response.data);
    console.log(response);
  };

  // should
  // const getProducts = () => {
  //   axios.get("https://hama-be.vercel.app/api/products").then((res) => {
  //     setProducts(res.data);
  //   });
  // };

  useEffect(() => {
    getProducts();
  }, []);

  return (
    <div className="App">
      {products.map((product) => (
        <div key={product.id}>
          <img src={product.images[0]} alt="" />
          <h1>{product.name}</h1>
          <p>{product.price}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
