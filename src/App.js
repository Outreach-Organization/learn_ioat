import React, { useState } from 'react';
import Plant from './Plant';
import dryImage from './dry.png';
import moistImage from './moist.png';
import wetImage from './wet.png';
import './App.css';

const App = () => {
  const [currentPlantIndex, setCurrentPlantIndex] = useState(0);
  const plants = [
    { id: 1, moistureLevel: 50 },
    { id: 2, moistureLevel: 80 },
    { id: 3, moistureLevel: 20 }
  ];

  const nextPlant = () => {
    setCurrentPlantIndex(prevIndex => (prevIndex + 1) % plants.length);
  };

  return (
    <div className="App">
      <h1>Hydro Heroes: Sorghum Sprout Sprint</h1>
      <div className="PlantContainer">
        <Plant
          key={plants[currentPlantIndex].id}
          moistureLevel={plants[currentPlantIndex].moistureLevel}
          dryImage={dryImage}
          moistImage={moistImage}
          wetImage={wetImage}
          goalId={plants[currentPlantIndex].id}
          onNextPlant={nextPlant}
        />
      </div>
      <footer>
        <p>© 2023 ShakoorLab</p>
      </footer>
    </div>
  );
};

export default App;

