import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";
import './css/index.css';
import './css/my_config.css';
import './css/normalize.css';

import './css/parts/header.css';
import './css/parts/footer.css';


import ArticlesApp from './apps/ArticlesApp';
import GamesApp from './apps/GamesApp';
import reportWebVitals from './reportWebVitals';


const Routing = () => {
  return(
    <Router>
      <Routes>
        <Route exact path="articles/"  element={<ArticlesApp />} />
        <Route exact path="games/" element={<GamesApp />}/>
      </Routes>
    </Router>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <Routing />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
