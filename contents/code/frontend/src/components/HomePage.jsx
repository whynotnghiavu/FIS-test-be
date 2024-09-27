import React, { useEffect, useState } from "react";

const HomePage = () => {
  const [posts, setPosts] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  // Fetch posts from the API
  const fetchPosts = async () => {
    try {
      const response = await fetch(
        "https://127.0.0.1:8000/api/v1/posts?skip=0&limit=100"
      );
      const data = await response.json();
      if (response.ok) {
        setPosts(data);
      } else {
        throw new Error(data.detail || "Failed to fetch posts");
      }
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="container mt-5">
      <h2>Posts</h2>
      {loading && <div>Loading...</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      {posts.length === 0 && !loading && <div>No posts found.</div>}
      {posts.map((post) => (
        <div key={post.id} className="card mb-4">
          <div className="card-body">
            <h5 className="card-title">{post.title}</h5>
            <p className="card-text">{post.content}</p>
            <p className="card-text">
              <small>
                By User ID: {post.user_id} on{" "}
                {new Date(post.created_at).toLocaleDateString()}
              </small>
            </p>  <p className="card-text">
              <small>
              Category ID: {post.category_id}  
              </small>
            </p>
            <Comments postId={post.id} />
          </div>
        </div>
      ))}
    </div>
  );
};

const Comments = ({ postId }) => {
  const [comments, setComments] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  // Fetch comments for a specific post
  const fetchComments = async () => {
    try {
      const response = await fetch(
        `https://127.0.0.1:8000/api/v1/posts/${postId}/comments`
      );
      const data = await response.json();
      if (response.ok) {
        setComments(data);
      } else {
        throw new Error(data.detail || "Failed to fetch comments");
      }
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchComments();
  }, [postId]);

  return (
    <div>
      <h6>Comments</h6>
      {loading && <div>Loading comments...</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      {comments.length === 0 && !loading && <div>No comments found.</div>}
      {comments.map((comment) => (
        <div key={comment.id} className="border p-2 mb-2">
          <p>
            <strong>
              {comment.user_id}
<br/>
            </strong>
              {comment.text}
          </p>
        </div>
      ))}
    </div>
  );
};

export default HomePage;

