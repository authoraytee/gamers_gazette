import React, { Component } from 'react';
import axios from 'axios';



class ArticlesApp extends Component {
    state = {
      articles: []
    };

    componentDidMount() {
      this.getArticles();
    }

    getArticles() {
      axios
        .get('http://127.0.0.1:8000/api/articles/')
        .then(res => {
          this.setState({articles: res.data });
        })
        .catch(err => {
            console.log(err);
        });
    }

    render() {
        return ( 
            <div> 
              <h1>Articles</h1>
              {this.state.articles.map(item => ( 
                  <div key = {item.id}>
                      <h4>{item.id}</h4> 
                      <h1>{item.title}</h1> 
                      <p>{item.link}</p>
                      <p>{item.text}</p>
                      <p>{item.site}</p>
                      <p>{item.pub_date}</p>
                      <hr></hr>
                  </div>
              ))} 
            </div>
        );
    }
}
export default ArticlesApp;