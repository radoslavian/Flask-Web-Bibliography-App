"Database models for the application."

from app import db

class Permissions:
    # save bibliography items to a list:
    SAVE_TO_LIST = 1
    EDIT_BIBLIOGRAPHY = 2
    ADMIN = 4


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, unique=True, nullable=False,
                   primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
#    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions += perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return f'<Role {self.name}>'


class User:
    pass


class Document(db.Model):
    __tablename__ = 'documents'
    document_id = db.Column(db.Integer, primary_key=True)

    document_type_id = db.Column(
        db.Integer, db.ForeignKey('document_types.type_id'))
    #document_type = db.relationship()

    # language_id = db.relationship()
    # original_language_id = db.relationship()

    from sqlalchemy.ext.associationproxy import association_proxy

    _master_doc = association_proxy('master_document', 'dependent_doc')
    _dependent_docs = association_proxy('dependent_docs', 'master_doc')

    title_proper = db.Column(db.String(255))
    parallel_title = db.Column(db.String(255))
    other_title_inf = db.Column(db.String(255))
    edition_statement = db.Column(db.String(40))
    parallel_edition_stmt = db.Column(db.String(40))

    # text field length:
    # Model.column.property.columns[0].type.length

    additional_edition_stmt = db.Column(db.String(40))
    numbering = db.Column(db.String(70))
    publication_date = db.Column(db.String(10))
    pagination = db.Column(db.String(30))
    physical_details = db.Column(db.String(45))
    dimensions = db.Column(db.String(60))
    accompanying_material = db.Column(db.String(60))

    # for more rudimentary series; separate relationship
    # for series defined as a document

    series = db.Column(db.String(45))
    note = db.Column(db.String(5000))
    issn = db.Column(db.String(9))
    isbn_10 = db.Column(db.String(13))
    isbn_13 = db.Column(db.String(17))


class RelatedDocuments(db.Model):
    "Self-referential relationship table for the documents table."

    __tablename__ = 'related_documents'
    master_doc_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'), primary_key=True)
    dependent_doc_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'), primary_key=True)
    description = db.Column(db.String(45))
    ordering = db.Column(db.Integer, default=0)

    dependent_doc = db.relationship(
        Document,
        primaryjoin=(dependent_doc_id == Document.document_id),
        backref='master_document')
    master_doc = db.relationship(
        Document,
        primaryjoin=(master_doc_id == Document.document_id),
        backref='dependent_docs')



class DocumentType(db.Model):
    __tablename__ = 'document_types'
    
    type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(200))
