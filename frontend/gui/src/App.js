import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import axios from 'axios';
import { API_ARTICLE_LIST_URL } from './constants/ApiUrls';
import Content from './components/content/Content';
import Navbar from "./components/navbar/Navbar";
import Footer from "./components/footer/Footer";
import DetailArticle from './components/detailArticle/DetailArticle';

class App extends Component {
  state = {
    articles: [],
    isLoading: true
  }

  componentDidMount = () => {
    this.setState({
      isLoading: true
    })
    axios.get(API_ARTICLE_LIST_URL).then(response => {
      this.setState({
        articles: response.data,
        isLoading: false
      }
      )
    })
  }

  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Navbar />
          <div className="container">
            <Route exact path="/"
              render={(props) => <Content articles={this.state.articles} />}
            />
            <Route path="/article/:slug/" component={DetailArticle} />
          </div>
          <Footer />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;