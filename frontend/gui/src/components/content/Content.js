import React from 'react';
import { Link } from 'react-router-dom';
import { API_ARTICLE_DETAIL_URL } from '../../constants/ApiUrls';
import axios from 'axios';

const Content = ({ articles }) => {

    const articlesList = articles.length ? (
        articles.map(article => {
            return (
                <div className="article-container" key={article.id} >
                    <div className="card text-center">
                        <div className="card-header">
                            Article
                        </div>
                        <div className="card-body">
                            <h5 className="card-title">{article.title}</h5>
                            <p className="card-text">{article.text.slice(0, 200) + " ..."}</p>
                            <Link to={'/' + 'article/' + article.pk} class="btn btn-primary">Read more...</Link>
                        </div>
                        <div className="card-footer text-muted">
                            {article.postedDate}
                        </div>
                    </div>
                </div>
            )
        })
    ) : (
            <p>There aren't any articles</p>
        )

    return (
        <div className="articles" >
            {console.log(articlesList)}
            {articlesList}
            {console.log(axios.get('http://127.0.0.1:8000/api/1'))}
        </div>
    );
}

export default Content;
