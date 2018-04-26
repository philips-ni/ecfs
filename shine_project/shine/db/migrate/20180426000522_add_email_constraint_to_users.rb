class AddEmailConstraintToUsers < ActiveRecord::Migration[5.2]
  def up
    execute %{
      ALTER TABLE
      users
      ADD CONSTRAINT
      email_must_be_company_email
      CHECK ( email ~* '^[^@]+@veritas\\.com$' )
    }
  end

  def down
    execute %{
      ALTER TABLE
      users
      DROP CONSTRAINT
      email_must_be_company_email
    }
  end
  
end
