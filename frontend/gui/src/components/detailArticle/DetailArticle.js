import React, { Component } from 'react';
import axios from 'axios';
import { API_ARTICLE_DETAIL_URL } from '../../constants/ApiUrls';
import { Link } from "react-router-dom";

const loadArticleFromApi = (slug) => {
    let url = API_ARTICLE_DETAIL_URL + slug;

    return axios.get(url)
}

class DetailArticle extends Component {
    state = {
        isLoading: true,
        article: {}
    }
    loadSingleArticle = (slug) => {
        this.setState({
            isLoading: true
        })
        loadArticleFromApi(slug).then((response) => {
            this.setState({
                isLoading: false,
                article: response.data[0]
            })
        })
    }


    componentDidMount = () => {
        let slug = this.props.match.params.slug;
        this.loadSingleArticle(slug)
    }

    render() {
        return (
            <div className='article-detail'>
                <div className="card" style="width: 18rem;">
                    {/* <img src={"https://picsum.photos/" + '1' + "/237/200/300"} class="card-img-top" alt="Article image" /> */}
                    <div className="card-body">
                        <h5 className="card-title">article.title</h5>
                        <p className="card-text">article.text</p>
                        <Link to="/" className="btn btn-primary">Back to Home page</Link>
                    </div>
                </div>
            </div>
        );
    }
}

export default DetailArticle;