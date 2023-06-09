/* eslint-disable jsx-a11y/alt-text */
import React, { useState } from 'react';
import axios from 'axios';

function FrecuenciaCompra() {
  const SUCURSALES = {
    SAN_SALVADOR: 'San Salvador',
    SOYAPANGO: 'Soyapango',
    SANTA_TECLA: 'Santa Tecla',
    DELGADO: 'Delgado',
    ILOPANGO: 'Ilopango',
    MEJICANOS: 'Mejicanos'
  };
  const PRODUCTOS = {
    TV: 'Televisor',
    SMARTPHONE: 'Teléfono inteligente',
    LAPTOP: 'Portátil',
    HEADPHONES: 'Audífonos',
    CAMERA: 'Cámara',
    SMARTWATCH: 'Reloj inteligente',
    SPEAKERS: 'Altavoces',
    GAMING_CONSOLE: 'Consola de videojuegos',
    BLENDER: 'Licuadora',
    VACUUM_CLEANER: 'Aspiradora',
    COFFEE_MACHINE: 'Máquina de café'
  };

  const [reporte, setReporte] = useState(null);
  async function handleFilter(e) {
      // Prevent the browser from reloading the page
      e.preventDefault();
      // Read the form data
      const form = e.target;
      const formData = new FormData(form);
      const formJson = Object.fromEntries(formData.entries());
      console.log(formJson); 
      await axios.post('http://localhost:8000/api/frecuenciaCompra/', formJson,{
        headers: {
            'Content-Type': 'application/json'
        }
      } ).then((response) => {
        setReporte(JSON.stringify(response.data, null, 4));
      });
  }
  return(
    <div className="container">
        <h2 className='text-center'>Frecuencia de compra</h2>
        <div className="row">
            <div className="col-md-auto">
                <form method="post" onSubmit={handleFilter}>
                    <h5>Seleccione los filtros necesarios</h5>
                    <label className="form-label mt-2">Sucursal:</label>
                    <select name='filterSucursal' className="form-select">
                        {Object.keys(SUCURSALES).map((suc) => (
                        <option key={suc} value={suc}>
                            {SUCURSALES[suc]}
                        </option>
                        ))}
                    </select>
                    <label className="form-label mt-2">Producto:</label>
                    <select name='filterProducto' className="form-select">
                        {Object.keys(PRODUCTOS).map((pro) => (
                        <option key={pro} value={pro}>
                            {PRODUCTOS[pro]}
                        </option>
                        ))}
                    </select>
                    <div className="d-grid gap-2 mt-4">
                        <button type="submit" className="btn btn-primary">Mostrar resultados</button>
                    </div>
                </form>
            </div>
            {reporte ? (
                    <>
                    <div className="col-md ps-5 reporte" >
                        <pre>{reporte}</pre>
                    </div></>
                    ):
                    <>
                    <div className="col-md text-center reporte" >
                        <img src='Waiting-amico.png' alt='Waiting' style={{ width: '30%', marginTop: '30px' }}></img><h2>Seleccione los filtros necesarios...</h2>
                    </div>
                    </>
                }
        </div>
    </div>
);
}

export default FrecuenciaCompra;