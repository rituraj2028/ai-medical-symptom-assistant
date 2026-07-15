import "./Navbar.css";

function Navbar(){
    return (
        <nav className = "navbar">
            <div className="logo">
                AI Medical Assistant
            </div>
            <div className = "nav-links">
                <a href="/">Home</a>
            </div>
        </nav>
    );
}

export default Navbar;