
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Upload = antd.Upload, Icon = antd.Icon, Modal = antd.Modal;
var PicturesWall = /** @class */ (function (_super) {
    __extends(PicturesWall, _super);
    function PicturesWall() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = {
            previewVisible: false,
            previewImage: '',
            fileList: [{
                    uid: -1,
                    name: 'clinic.png',
                    status: 'done',
                    url: 'img/doctor-profile.jpg'
                }]
        };
        _this.handleCancel = function () { return _this.setState({ previewVisible: false }); };
        _this.handlePreview = function (file) {
            _this.setState({
                previewImage: file.url || file.thumbUrl,
                previewVisible: true
            });
        };
        _this.handleChange = function (_a) {
            var fileList = _a.fileList;
            console.log(fileList.slice());
            _this.setState({ fileList: fileList });
        };
        return _this;
    }
    PicturesWall.prototype.render = function () {
        var _a = this.state, previewVisible = _a.previewVisible, previewImage = _a.previewImage, fileList = _a.fileList;
        var uploadButton = (React.createElement("div", null,
            React.createElement(Icon, { type: "plus" }),
            React.createElement("div", { className: "ant-upload-text" }, "Upload")));
        return (React.createElement("div", { className: "clearfix" },
            React.createElement(Upload, { action: "//jsonplaceholder.typicode.com/posts/", listType: "picture-card", fileList: fileList, onPreview: this.handlePreview, onChange: this.handleChange }, fileList.length >= 10 ? null : uploadButton),
            React.createElement(Modal, { visible: previewVisible, footer: null, onCancel: this.handleCancel },
                React.createElement("img", { alt: "example", style: { width: '100%' }, src: previewImage }))));
    };
    return PicturesWall;
}(React.Component));
ReactDOM.render(React.createElement(PicturesWall, null), mountNode);
