import React, { Component } from 'react';
import axios from 'axios';



class GamesApp extends Component {
    state = {
      games: []
    };

    componentDidMount() {
      this.getGames();
    }

    getGames() {
      axios
        .get('http://127.0.0.1:8000/api/games/')
        .then(res => {
          this.setState({games: res.data });
        })
        .catch(err => {
            console.log(err);
        });
    }

    render() {
        return ( 
            <div> 
                <h1>Games</h1>
                {this.state.games.map(item => ( 
                    <div key = {item.id}>
                        <h4>{item.id}</h4> 
                        <h1>{item.name}</h1> 
                        <p>{item.release_date}</p>
                        <p>{item.metacritic_rating}</p>
                        <p>{item.esb_rating}</p>
                        <hr></hr>
                    </div>
              ))} 
            </div>
        );
    }
}

export default GamesApp;